from pageobject.landingpage import LandingPage
from pageobject.aboutpage import AboutPage
from pageobject.searchpage import SearchPage
from pageobject.loginpage import LoginPage
from webdriver.Chrome import ChromeBrowser


class Factory:

    landingpage = LandingPage(ChromeBrowser().page)
    aboutpage = AboutPage(ChromeBrowser().page)
    searchpage = SearchPage(ChromeBrowser().page)
    loginpage = LoginPage(ChromeBrowser().page)
