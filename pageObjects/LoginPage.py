from playwright.sync_api import sync_playwright, Playwright, BrowserContext, Page


class LoginPage:
    txtbox_username_id = 'get_by_label("Email:")'
    txtbox_password_id = 'get_by_label("Password:")'
    btn_login_role = 'get_by_role("button", name="Log in")'
    failed_error_message = '//div[contains(text(), "Login was unsuccessful. Please correct the errors and try")]'
    btn_logout_role = 'get_by_role("link", name="Logout")'

    def __init__(self, page: Page):
        self.page = page

    def setusername(self, username):
        self.page.locator(self.txtbox_username_id).clear()
        self.page.locator(self.txtbox_username_id).type(username)

    def setpassword(self, password):
        self.page.locator(self.txtbox_password_id).clear()
        self.page.locator(self.txtbox_password_id).type(password)

    def clicklogin(self):
        self.page.locator(self.btn_login_role).click()

    def clicklogout(self):
        self.page.locator(self.btn_logout_role).click()
