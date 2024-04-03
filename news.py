import requests
from bs4 import BeautifulSoup

#topic = ['WORLD', 'NATION', 'BUSINESS', 'TECHNOLOGY', 'ENTERTAINMENT', 'SCIENCE', 'SPORTS', 'HEALTH']

class GoogleNews:
    def __init__(self, ticker = 'GOOG', topic = True) -> None:
        '''
        ticker - company name, default 'GOOG'
        topic - show BUSINESS news, default True
        
        feeds - created automatically when ticker is provided
        '''
        self.ticker = ticker
        self.topic = topic
        self.feeds, self.error_message = self.__get_feeds()
        
        # Check if data fetched successfully
        if self.feeds is None:
            print(self.error_message)

    def __get_url(self):
        '''
        Get Google News RSS feed url 
        '''
        BASE_URL = 'https://news.google.com/rss/'

        if self.topic:
            t = 'BUSINESS'
            url = f'{BASE_URL}headlines/section/topic/{t}?q={self.ticker}&hl=en-US&gl=US&ceid=US:en'
        else:
            url = f'{BASE_URL}search?q={self.ticker}&hl=en-US&gl=US&ceid=US:en'
        
        # intitle search
        return url
    
    def __get_feeds(self):
        '''
        1. Make GET request and retrieve data as XML file
        2. Parse XML to find all news feeds (labeled as <item> in XML)
        3. Handle error events
        '''
        try:    
            response = requests.get(self.__get_url())

            if response.status_code == requests.codes.ok:
                feeds_xml = BeautifulSoup(response.text, 'xml')
                feeds = feeds_xml.find_all('item')
                n_articles = len(feeds)
                print(f'Data loaded successfully.\n{n_articles} articles found.')
                return feeds, None

            else:
                message = f'Status code : {response.status_code}\nError message : {response.text}'
                return None, message
            
        except requests.exceptions.RequestException as e:
            return None, str(e)
        
    def get_titles(self):
        '''
        1. Get all news titles
        2. Return in List
        '''
        if self.feeds is None:
            print(self.error_message)
            return None
        else:
            titles = [each.title.text for each in self.feeds]
            return titles

    def get_urls(self):
        '''
        1. Get all news urls
        2. Return in List
        '''
        if self.feeds is None:
            print(self.error_message)
            return None
        else:
            urls = [each.link.text for each in self.feeds]
            return urls

    def get_sources(self):
        '''
        1. Get all news source
        2. Return in List
        '''
        if self.feeds is None:
            print(self.error_message)
            return None
        else:
            sources = [each.source.text for each in self.feeds]
            return sources
        
    def get_dict(self):
        '''
        1. Get all news titles, urls, and source
        2. Return in Dictionary
        '''
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


if __name__ == '__main__':
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
    pass