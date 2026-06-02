import playwright
import pytest
from playwright.sync_api import sync_playwright

#Step 1: Choose Browser / Supported browser
SUPPORTED_BROWSERS = ["chromium", "firefox", "webkit", "safari" ,"edge"]

# Step 2: Define the browser
BROWSER_NAME = "chromium"

#Step 3: URL
URL = "https://www.google.com"

HEADLESS = True

#Step 4: Setup + Teardown
@pytest.fixture(scope="class")
def setup(request):
    print("Setting up browser : ", BROWSER_NAME)

    # Step 5: Start Playwright
    playwright = sync_playwright().start()

    #Step 6: Launch the browser
    if BROWSER_NAME == "chromium":
        browser = playwright.chromium.launch(headless=HEADLESS)
    elif BROWSER_NAME == "firefox":
        browser = playwright.firefox.launch(headless=HEADLESS)
    elif BROWSER_NAME == "webkit":
        browser = playwright.webkit.launch(headless=HEADLESS)
    else:
        raise ValueError(f"Browser {BROWSER_NAME} is not supported.")

    # Step 7: create browser context
    context = browser.new_context()

    # Step 8: Create a new page
    page = context.new_page()

    # Viewport - Screen Size
    page.set_viewport_size({"width":1920, "height":1080})

    # Step 9: Open the URL
    page.goto(URL)

    request.cls.page = page

    # YIELD = Tests Run Here.....
    yield

    # Teardown
    context.close()
    browser.close()
    playwright.stop()

@pytest.mark.usefixtures("setup")
class TestOpenBrowser:
    def test_open_browser(self):
        self.page.wait_for_timeout(2000)
        tittle = self.page.title()
        print("Page Tittle is : ",tittle)


