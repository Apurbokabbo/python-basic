import pytest
from playwright.sync_api import sync_playwright

#Step 1: Choose Browser / Supported browser
SUPPORTED_BROWSERS = ["chromium", "firefox", "webkit"]

# Step 2: Define the browser
BROWSER_NAME = "chromium"

#Step 3: URL
URL = "https://automation.ebrahimhossain.com.bd/form.html"

#Step 4: Setup + Teardown

@pytest.fixture(scope="class")
def setup(request):
    print(f"Starting {BROWSER_NAME} browser....")

    # Step 5: Start Playwright
    playwright = sync_playwright().start()

    #Step 6: Launch the browser
    if BROWSER_NAME == "chromium":
        browser = playwright.chromium.launch(headless=False)
    elif BROWSER_NAME == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif BROWSER_NAME == "webkit":
        browser = playwright.webkit.launch(headless=False)
    else:
        raise ValueError(f"Browser {BROWSER_NAME} is not supported.")

    # Step 7: create browser context
    context = browser.new_context()

    #Step 8: Create a new page
    page = context.new_page()

    #Step 9: Open the URL
    page.goto(URL)

    request.cls.page = page

    # YIELD = Tests Run Here.....
    yield

    # Teardown
    context.close()
    browser.close()
    playwright.stop()


@pytest.mark.usefixtures("setup")
class TestAddCookies:
    def test_add_cookies(self):
        self.page.wait_for_timeout(2000) # 2 seconds
        cookie = {"name": "test", "value": "test_value"}
        self.page.context.add_cookies([cookie])

        cookies = self.page.context.cookies()
        cookies_name = [c["name"] for c in cookies]
        print(cookies_name)

