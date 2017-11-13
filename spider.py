from urllib.request import urlopen
from link_finder import LinkFinder
from file_handling import *

class Spider:

    # Class variables
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue_set = set()
    crawled_set = set()

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'

        self.setup()
        self.crawl_page('Spider 0', Spider.base_url)

    @staticmethod
    def setup(self):
        setup_dir(Spider.project_name)
        initialize_url_lists(Spider.project_name, Spider.base_url)
        Spider.queue_set = file_to_set(Spider.queue_file)
        Spider.crawled_set = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled_set:
            print(thread_name + ' crawling ' + page_url)

    @staticmethod
    def gather_urls(page_url):
        string_html = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html:':
                byte_html = response.read()
                string_html = byte_html.decode('utf-8') #todo: fine?
                finder = LinkFinder(Spider.base_url, page_url)
                finder.feed(string_html)
        except:
            print('ERROR: crawl unsuccessful - url list empty')
            return set()

        return finder.get_urls()

    @staticmethod
    def add_urls_to_queue(urls):
        for url in urls:
            # if url in Spider.queue_set:
                # continue
            # if url in Spider.crawled_set:
                # continue
            # if Spider.domain_name not in url:
                # continue
            if url in Spider.queue_set or url in Spider.crawled_set or Spider.domain_name not in url:
                continue
            Spider.queue_set.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue_set, Spider.queue_file)
        set_to_file(Spider.crawled_set, Spider.crawled_file)

