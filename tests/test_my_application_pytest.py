from playwright.sync_api import Page, expect
from factory.factory import Factory
from time import sleep
from webdriver.Chrome import ChromeBrowser
import pytest

class TestMyApp:

    @pytest.mark.order(2)
    def test_username_alert(self):
        Factory.loginpage._login_button.click()
        expect(Factory.loginpage._username_required_alert).to_be_visible()


    @pytest.mark.skip
    def test_python_about_getting_started(self):
        Factory.landingpage.click_about_link()
        expect(Factory.aboutpage._getting_started_title).to_contain_text('Getting Started')

    
    @pytest.mark.skip
    def test_search_criteria(self):
        Factory.landingpage._input_search.fill('test')
        Factory.landingpage._go_button.click()
        expect(Factory.searchpage._no_results_found).not_to_be_visible()

   
    @pytest.mark.order(1)
    def test_login_to_inventory(self, params):
        Factory.loginpage.login_to_sauce_iventory(params)
        expect(ChromeBrowser().page).to_have_url('https://www.saucedemo.com/inventory.html')
