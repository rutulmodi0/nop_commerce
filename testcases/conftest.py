import pytest
from playwright.sync_api import sync_playwright

baseURL = 'https://admin-demo.nopcommerce.com'


@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        # context = browser.new_context(record_video_dir='D:/nop_commerce/References')
        context = browser.new_context()
        yield context
        context.close()




@pytest.fixture(scope="function")
def setup(browser_context):
    page = browser_context.new_page()
    page.goto(baseURL)
    yield page
    page.close()
