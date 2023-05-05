from pageobject.landingpage import LandingPage
from webdriver.Chrome import ChromeBrowser


class Factory:

    landingpage = LandingPage(ChromeBrowser().page)
