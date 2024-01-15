import pytest, pytest_dependency
from playwright.sync_api import sync_playwright, Playwright, Page, expect
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import *


class Test_001_Login:

    username = ReadProperties.getuseremail()
    password = ReadProperties.getpassword()

    @pytest.mark.dependency(depends=['test_login_successful'])
    def test_check_url(self, setup):
        self.page = setup
        get_title = self.page.title()
        if get_title == "Your store. Login":
            assert True
        else:
            self.page.screenshot(path="D:/nop_commerce/References/test_check_url.jpg")
            assert False

    @pytest.mark.xfail
    def test_login_failed(self, setup):
        self.page = setup
        lp = LoginPage(self.page)
        lp.setusername("wrong@gmail.com")
        lp.setpassword(self.password)
        lp.clicklogin()
        get_title = self.page.locator(lp.failed_error_message).text_content()
        if get_title == "Login was unsuccessful. Please correct the errors and try again.":
            assert True
        else:
            assert False

    @pytest.mark.dependency
    def test_login_successful(self, setup):
        self.page = setup
        lp = LoginPage(self.page)
        lp.setusername(self.username)
        lp.setpassword(self.password)
        lp.clicklogin()
        get_title = self.page.title()
        if get_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            self.page.screenshot(path="D:/nop_commerce/References/test_login_successful.jpg")
            assert False
