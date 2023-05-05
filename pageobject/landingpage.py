from playwright.sync_api import Page
from pageobject.base import Base
from webdriver.Chrome import ChromeBrowser

class LandingPage:

    def __init__(self, page):
        self.page = page
        self._about_link = self.page.locator("(//a[@href='/about/'])[1]")
    

    def click_about_link(self):
        self._about_link.click()

