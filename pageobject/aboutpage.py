from playwright.sync_api import Page, expect
from pageobject.base import Base
from webdriver.Chrome import ChromeBrowser
from time import sleep


class AboutPage:

    def __init__(self, page):
        self.page = page
        self._getting_started_title = self.page.locator("//h2[text()='Getting Started']")

    
