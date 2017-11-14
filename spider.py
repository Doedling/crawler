from urllib.request import urlopen
from urllib.error import HTTPError
from link_finder import LinkFinder
from file_handling import *
import traceback
from bs4 import BeautifulSoup
import requests

class Spider:

    # Class variables
    project_name = ''
    base_url = ''
    # domain_name = ''
    wait_file = ''
    crawled_file = ''
    address_file = ''
    wait_set = set()
    crawled_set = set()
    address_set = set()

    # def __init__(self, project_name, base_url, domain_name):
    def __init__(self, project_name, base_url):
        Spider.project_name = project_name
        Spider.base_url = base_url
        # Spider.domain_name = domain_name
        Spider.wait_file = Spider.project_name + '/waiting.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        Spider.address_file = Spider.project_name + '/addresses.txt'

        self.setup()
        # self.crawl_page('Spider 0', Spider.base_url)
        self.crawl_page(Spider.base_url)

    @staticmethod
    def setup():
        setup_dir(Spider.project_name)
        initialize_files(Spider.project_name, Spider.base_url)
        Spider.wait_set = file_to_set(Spider.wait_file)
        Spider.crawled_set = file_to_set(Spider.crawled_file)

    @staticmethod
    # def crawl_page(thread_name, page_url):
    def crawl_page(page_url):
        if page_url not in Spider.crawled_set:
            # print(thread_name + ' crawling ' + page_url)
            print(' crawling ' + page_url)
            Spider.add_urls_to_waitinglist(Spider.gather_urls(page_url))
            # Spider.search_for_urls(page_url)
            Spider.wait_set.remove(page_url)
            Spider.crawled_set.add(page_url)
            Spider.update_files()

    @staticmethod
    def gather_urls(page_url):
        string_html = ''
        finder = LinkFinder(Spider.base_url, page_url)
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                byte_html = response.read()
                string_html = byte_html.decode('utf-8') #todo: fine?
                finder.feed(string_html)
        except HTTPError:
            print('HTTP ERROR: crawl unsuccessful - created empty url list from ' + page_url)
            return set()

        Spider.address_set = finder.get_addresses()
        return finder.get_urls()

    @staticmethod
    def search_for_urls(page_url):
        print('searching url ' + page_url)
        res = requests.get(page_url)
        content = res.text
        soup = BeautifulSoup(content, 'html.parser')
        for url in soup.find_all('a', 'href'):
            print('met an url: ' + url)
            if 'mailto' in url:
                Spider.address_set.add(url)
            else:
                Spider.add_single_url_to_waitinglist(url)


    @staticmethod
    def add_urls_to_waitinglist(urls):
        for url in urls:
            # if url in Spider.wait_set or url in Spider.crawled_set or Spider.base_url not in url:
            if url in Spider.wait_set or url in Spider.crawled_set or Spider.base_url + 'research' not in url:
                continue
            Spider.wait_set.add(url)

    @staticmethod
    def add_single_url_to_waitinglist(url):
        # if url in Spider.wait_set or url in Spider.crawled_set or Spider.base_url not in url:
        if url in Spider.wait_set or url in Spider.crawled_set or Spider.base_url + 'research' not in url:
            print('nothing new')
        Spider.wait_set.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.wait_set, Spider.wait_file)
        set_to_file(Spider.crawled_set, Spider.crawled_file)
        append_set_to_file(Spider.address_set, Spider.address_file)
        # set_to_file(Spider.address_set, Spider.address_file)

