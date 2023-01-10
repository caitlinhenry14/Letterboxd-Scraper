from list_scraper import *

class List:
    
    def __init__(self, list_name, link):
        
        self.name = list_name
        self.link = link
        print("\nScraping list data...\n")
        self.films = scrape_list(self.link)