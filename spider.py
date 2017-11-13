from urllib.request import urlopen
from link_finder import LinkFinder
from file_handling import *

class Spider:

    # Class variables
    project_name = ''
    base_url = ''
    domain_name = ''
    wait_file = ''
    crawled_file = ''
    wait_set = set()
    crawled_set = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.wait_file = Spider.project_name + '/waiting.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'

        self.setup()
        self.crawl_page('Spider 0', Spider.base_url)

    @staticmethod
    def setup():
        setup_dir(Spider.project_name)
        initialize_url_lists(Spider.project_name, Spider.base_url)
        Spider.wait_set = file_to_set(Spider.wait_file)
        Spider.crawled_set = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled_set:
            print(thread_name + ' crawling ' + page_url)
            Spider.add_urls_to_waitinglist(Spider.gather_urls(page_url))
            Spider.wait_set.remove(page_url)
            Spider.crawled_set.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_urls(page_url):
        string_html = ''
        finder = LinkFinder(Spider.base_url, page_url)
        try:
            response = urlopen(page_url)
            print('Found: ' + response.getheader('Content-Type'))
            # if response.getheader('Content-Type') == 'text/html':
            if 'text/html' in response.getheader('Content-Type'):
                byte_html = response.read()
                string_html = byte_html.decode('utf-8') #todo: fine?
                # finder = LinkFinder(Spider.base_url, page_url)
                finder.feed(string_html)
        except:
            print('ERROR: crawl unsuccessful - created empty url list')
            return set()

        return finder.get_urls()

    @staticmethod
    def add_urls_to_waitinglist(urls):
        for url in urls:
            # if url in Spider.queue_set:
                # continue
            # if url in Spider.crawled_set:
                # continue
            # if Spider.domain_name not in url:
                # continue
            if url in Spider.wait_set or url in Spider.crawled_set or Spider.domain_name not in url:
                continue
            Spider.wait_set.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.wait_set, Spider.wait_file)
        set_to_file(Spider.crawled_set, Spider.crawled_file)

