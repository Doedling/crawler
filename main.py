# todo: will it crawl both DK and EN versions?
# todo: option for user to not input project name - then use domain name

import threading
from queue import Queue
from spider import Spider
from domain_locater import *
from file_handling import *

PROJECT_NAME = 'AU_CS_researchers'
ROOT_URL = 'http://cs.au.dk/research/'
DOMAIN_NAME = get_domain_name(ROOT_URL)
WAIT_FILE = PROJECT_NAME + '/waiting.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 4
thread_queue = Queue()

Spider(PROJECT_NAME, ROOT_URL, DOMAIN_NAME)


def crawl():
    waiting_list = file_to_set(WAIT_FILE)
    if len(waiting_list) > 0:
        start_jobs()
    else:
        print("--- DONE ---")


def start_jobs():
    for link in file_to_set(WAIT_FILE): #todo: fix redundancy
        thread_queue.put(link)
    thread_queue.join()
    crawl()


def create_spider_threads():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target = work)
        t.daemon = True
        t.start()


def work():
    while True:
        url = thread_queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        thread_queue.task_done()


create_spider_threads()
crawl()