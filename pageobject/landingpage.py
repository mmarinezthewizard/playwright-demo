from playwright.sync_api import Page
from pageobject.base import Base
from webdriver.Chrome import ChromeBrowser

class LandingPage:

    def __init__(self, page):
        self.page = page
        self._about_link = self.page.locator("(//a[@href='/about/'])[1]")
        self._input_search = self.page.locator("input[id='id-search-field']")
        self._go_button = self.page.locator("button[class='search-button']")
    

    def click_about_link(self):
        self._about_link.click()



