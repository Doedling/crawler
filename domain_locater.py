from urllib.parse import urlparse


def get_domain_name(url):
    try:
        location_path = urlparse(url).netloc  # get network location
        path_elements = location_path.split('.')
        return path_elements[-2] + '.' + path_elements[-1]  # extract last part of network location
    except:
        print('ERROR: unsuccessful attempt to get domain name')
        return ''
