import time

import pytest
from playwright.sync_api import sync_playwright

#Step 1: Choose Browser / Supported browser
SUPPORTED_BROWSERS = ["chromium", "firefox", "webkit"]

# Step 2: Define the browser
BROWSER_NAME = "chromium"

#Step 3: URL
URL = "https://www.google.com"

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
class TestNavigation:
    def test_navigation(self):
        title  = self.page.title()
        print(f"Title: {title}")
        # Open the 2nd URL
        self.page.goto("https://playwright.dev/python/docs/api/class-browsercontext")
        title = self.page.title()
        print(f"Title: {title}")
        # Back - 1st URL
        print("Moving back....")
        self.page.go_back(wait_until="load")
        self.page.wait_for_timeout(2000)  # 2 seconds

        # Forward - 2nd URL
        print("Moving Forward....")
        self.page.go_forward(wait_until="load")
        self.page.wait_for_timeout(2000)  # 2 seconds

        print(f"Refreshing the page....")
        self.page.reload(wait_until="load")
        self.page.wait_for_timeout(2000)  # 2 seconds



