from urllib.parse import urlparse


def get_domain_name(url):
    try:
        location_path = urlparse(url).netloc  # get network location
        path_elements = location_path.split('.')
        domain_name = path_elements[-2] + '.' + path_elements[-1]
        print('DOMAIN NAME: ' + domain_name)
        return domain_name  # extract last part of network location
    except:
        print('ERROR: unsuccessful attempt to get domain name')
        return ''
