from playwright.sync_api import Page
from pageobject.base import Base
from webdriver.Chrome import ChromeBrowser
from time import sleep

class LoginPage:

    def __init__(self, page):
        self.page = page
        self._login_button = self.page.locator("input[value='Login']")
        self._username_required_alert = self.page.locator("//h3[text()='Epic sadface: Username is required']")
        self._password_required_alert = self.page.locator("//h3[text()='Epic sadface: Password is required']")
        self._invalid_credentials_alert = self.page.locator("//h3[text()='Epic sadface: Username and password do not match any user in this service']")
        self._input_username = self.page.locator("input[name='user-name']")
        self._input_password = self.page.locator("input[name='password']")


    def login_to_sauce_iventory(self, params):
        self._input_username.fill(params["appUser"])
        self._input_password.fill(params["appPassword"])
        self._login_button.click()


