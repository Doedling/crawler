from html.parser import HTMLParser
from urllib import parse


class LinkFinder(HTMLParser):

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.urls = set()
        self.addresses = set()
        self.nested = 0

    # Override
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    if 'mailto' in url:
                        email_address = url.split(':', 1)[1].split('?')[0]
                        self.addresses.add(email_address)
                    else:
                        self.urls.add(url)

        elif tag == 'div':
            self.nested += 1

    # Override
    def handle_endtag(self, tag):
        if tag == 'div' and self.nested > 0:
            self.nested -= 1

    # Override
    def handle_data(self, data):
        if self.nested > 0:
            if 'div' in data:
                print(data)

    def get_urls(self):
        return self.urls

    def get_addresses(self):
        return self.addresses

    # Basic implementation of abstract method in HTMLParser
    def error(self, message):
        pass
