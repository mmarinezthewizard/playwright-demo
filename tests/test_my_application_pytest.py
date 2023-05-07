from playwright.sync_api import Page
from factory.factory import Factory
from time import sleep
import pytest

class TestMyApp:

    def test_title(self):
        Factory.landingpage.click_about_link()

