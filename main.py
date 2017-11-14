# todo: will it crawl both DK and EN versions?
# todo: option for user to not input project name - then use domain name

from spider import Spider
# from domain_locater import *
from file_handling import *

PROJECT_NAME = 'AU_CS_researchers'
# ROOT_URL = 'http://cs.au.dk/research/'
ROOT_URL = 'http://cs.au.dk/'
# DOMAIN_NAME = get_domain_name(ROOT_URL)
WAIT_FILE = PROJECT_NAME + '/waiting.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
waiting_list = []

# Spider(PROJECT_NAME, ROOT_URL, DOMAIN_NAME)
Spider(PROJECT_NAME, ROOT_URL)


def crawl():
    while len(file_to_set(WAIT_FILE)) > 0: #todo: make solution non-ugly
        get_next(file_to_set(WAIT_FILE))
    print("--- DONE ---")


def get_next(url_set):
    # for link in file_to_set(WAIT_FILE):
    for url in url_set:
        waiting_list.append(url)
    current_url = waiting_list.pop()
    Spider.crawl_page(current_url)


crawl()