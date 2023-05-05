from playwright.sync_api import Page

class LoginPage():

    def type_user_email(page: Page):
        page.get_by_label("Email").fill("test@test.com")

