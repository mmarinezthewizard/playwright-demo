from playwright.sync_api import sync_playwright


class ChromeBrowser:
   # with sync_playwright() as webdriver:
    webdriver = sync_playwright().start()
    browser = webdriver.chromium.launch(channel="chrome", headless=False)
    page = browser.new_page()
        
    
