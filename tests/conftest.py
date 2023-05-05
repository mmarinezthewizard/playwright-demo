from webdriver.Chrome import ChromeBrowser
from time import sleep
import pytest


pytest_browser = None

# PYTEST COMMAND LINES VARIABLES
def pytest_addoption(parser):
    parser.addoption(
            "--appUrl", 
            action="store", 
            default="https://gloriatest-customer.greenlinknetworks.xyz/", 
            help="Application url"
            
            )

    parser.addoption(
            "--appUser", 
            action="store", 
            default="admin", 
            help="App user"

            )

    parser.addoption(
            "--appPassword", 
            action="store", 
            default="1234", 
            help="App password"

            )

# PYTEST VARIABLE ASSIGNMENTS 
@pytest.fixture
def params(request):
    params = {}
    params['appUrl'] = request.config.getoption("--appUrl")
    params['appUser'] = request.config.getoption("--appUser")
    params['appPassword'] = request.config.getoption("--appPassword")
    return params


def close_browser():
    print("close_browser")
    if pytest_browser is not None:
        pytest_browser.page.close()
        pytest_browser.webdriver.stop()



def setup_browser(url):
    print("setup_browser")
    
    global pytest_browser
    pytest_browser = ChromeBrowser()
    pytest_browser.page.goto(url)
    sleep(5)


@pytest.fixture(autouse=True)
def setup_and_teardown(params):

    setup_browser(params['appUrl'])

    yield

    close_browser()
