import os

### Auxiliary functions ###

# Create a new file
def write_file(path, content):
    fl = open(path, 'w') #write to file
    fl.write(content)
    fl.close()


# Add url to list
def add_url(path, new_url):
    with open(path, 'a') as file: #append to end of file
        file.write(new_url + '\n')


# Clear file
def empty_file(path):
    with open(path, 'w'): #overwrite file in path
        pass #add nothing to new file



### Setup functions ###

def setup():
    # Create working directory
    dir_name = 'AU_CS_researchers'
    crawl_url = 'http://cs.au.dk/research/'
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # Make sure there is are files to keep track of urls
    initialize_url_lists(dir_name, crawl_url)


def initialize_url_lists(folder_name, start_url):
    #initialize list of urls to crawl
    queue = folder_name + '/queue.txt'
    if not os.path.isfile(queue):
        write_file(queue, start_url + '\n')

    #initialize list of crawled urls
    crawled = folder_name + '/crawled.txt'
    if not os.path.isfile(crawled):
        write_file(crawled, '')



setup()