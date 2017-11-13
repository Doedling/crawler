# todo: will it crawl both DK and EN versions?
# todo: option for user to not input project name - then use domain name

# import threading
# from queue import Queue
from spider import Spider
from domain_locater import *
from file_handling import *

PROJECT_NAME = 'AU_CS_researchers'
ROOT_URL = 'http://cs.au.dk/research/'
DOMAIN_NAME = get_domain_name(ROOT_URL)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'

Spider(PROJECT_NAME, ROOT_URL, DOMAIN_NAME)
