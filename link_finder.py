from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.urls = set()
        self.addresses = set()

    # Override
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    if 'mailto' in url:
                        self.addresses.add(url)
                    else:
                        self.urls.add(url)

    def get_urls(self):
        return self.urls

    def get_addresses(self):
        return self.addresses

    # Basic implementation of abstract method in HTMLParser
    def error(self, message):
        pass
