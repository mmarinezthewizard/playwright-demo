from webdriver.Chrome import ChromeBrowser
from playwright.sync_api import sync_playwright


def playwright_driver(func):
    def wrapper(self, *args, **kwargs):
       func(self, ChromeBrowser().page)

    return wrapper

