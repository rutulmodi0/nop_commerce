import pytest
from playwright.sync_api import sync_playwright

baseURL = 'https://admin-demo.nopcommerce.com'


@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        # context = browser.new_context(record_video_dir='D:/nop_commerce/References')
        context = browser.new_context()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        yield context
        context.tracing.stop(path='trace.zip')
        context.close()


@pytest.fixture(scope="class")
def setup(browser_context):
    page = browser_context.new_page()
    page.goto(baseURL, wait_until="load")
    yield page
    page.close()
