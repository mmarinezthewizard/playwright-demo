from playwright.sync_api import Page, expect
from pageobject.base import Base
from webdriver.Chrome import ChromeBrowser
from time import sleep


class SearchPage:


    def __init__(self, page):
        self.page = page
        self._no_results_found = self.page.locator("ul > p")
     


