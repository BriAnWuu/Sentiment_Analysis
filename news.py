import requests
from bs4 import BeautifulSoup

#topic = ['WORLD', 'NATION', 'BUSINESS', 'TECHNOLOGY', 'ENTERTAINMENT', 'SCIENCE', 'SPORTS', 'HEALTH']

class GoogleNews:
    def __init__(self, ticker = 'GOOG', topic = False) -> None:
        self.ticker = ticker
        self.topic = topic
        self.feeds, self.error_message = self.__get_feeds()
        
        if self.feeds is None:
            print(self.error_message)

    def __get_url(self):
        if self.topic:
            t = 'BUSINESS'
            url = f'https://news.google.com/rss/headlines/section/topic/{t}?q={self.ticker}&hl=en-US&gl=US&ceid=US:en'
        else:
            url = f'https://news.google.com/rss/search?q={self.ticker}&hl=en-US&gl=US&ceid=US:en'
        
        # intitle search
        return url
    
    def __get_feeds(self):
        try:    
            response = requests.get(self.__get_url())

            if response.status_code == requests.codes.ok:
                feeds_xml = BeautifulSoup(response.text, 'xml')
                feeds = feeds_xml.find_all('item')
                return feeds, None

            else:
                message = f'Status code : {response.status_code}\nError message : {response.text}'
                return None, message
            
        except requests.exceptions.RequestException as e:
            return None, str(e)
        
    def get_titles(self):
        if self.feeds is None:
            print(self.error_message)
            return None
        else:
            titles = [each.title.text for each in self.feeds]
            return titles

    def get_urls(self):
        if self.feeds is None:
            print(self.error_message)
            return None
        else:
            urls = [each.link.text for each in self.feeds]
            return urls

    def get_sources(self):
        if self.feeds is None:
            print(self.error_message)
            return None
        else:
            sources = [each.source.text for each in self.feeds]
            return sources
        
    def get_dict(self):
        if self.feeds is None:
            print(self.error_message)
            return None
        else:
            titles = []
            urls = []
            sources = []

            for each in self.feeds:
                titles.append(each.title.text)
                urls.append(each.link.text)
                sources.append(each.source.text)

            dictionary = {
                'titles' : titles,
                'urls' : urls,
                'sources' : sources
            }
        return dictionary


# ticker = 'AAPL'
# a = GoogleNews(ticker, True)
# d = a.get_dict()
# l = a.get_titles()
# u = a.get_urls()
# s = a.get_sources()
# print(d)
# print(len(l))
# print(len(u))
# print(len(s))
