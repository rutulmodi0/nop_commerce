from playwright.sync_api import sync_playwright, Playwright, BrowserContext, Page


class LoginPage:
    txtbox_username_id = '//input[@id="Email"]'
    txtbox_password_id = '//input[@id="Password"]'
    btn_login_role = '//button[@class="button-1 login-button" and contains(@class, "login-button")]'
    failed_error_message = '//div[text()="Login was unsuccessful. Please correct the errors and try again."]'
    btn_logout_role = 'get_by_role("link", name="Logout")'

    def __init__(self, page: Page):
        self.page = page

    def setusername(self, username):
        self.page.locator(self.txtbox_username_id).clear()
        self.page.locator(self.txtbox_username_id).type(username)

    def setpassword(self, password):
        self.page.locator(self.txtbox_password_id).click()
        self.page.locator(self.txtbox_password_id).fill(password)

    def clicklogin(self):
        self.page.locator(self.btn_login_role).click()

    def clicklogout(self):
        self.page.locator(self.btn_logout_role).click()
