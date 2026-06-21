import pytest
from playwright.sync_api import sync_playwright
import time

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
    # page.goto(URL)

    request.cls.page = page

    # YIELD = Tests Run Here.....
    yield

    # Teardown
    context.close()
    browser.close()
    playwright.stop()


@pytest.mark.usefixtures("setup")
class TestJavascript:
    def test_zoom(self):
        self.page.goto(URL)
        self.page.evaluate("""
            document.body.style.zoom = '50%'
        """)
        time.sleep(5)

    def test_dimensions(self):
        self.page.goto(URL)
        dimensions = self.page.evaluate("""
            ()=>{
                return{
                    width: window.innerWidth,
                    height: window.innerHeight
                }
            }
        """)
        print(dimensions)
        time.sleep(5)

    def test_background(self):
        self.page.goto(URL)
        self.page.evaluate("""
            document.body.style.backgroundColor = 'green'
        """)
        time.sleep(5)

    def test_highlight_element(self):
        self.page.goto(URL)
        self.page.evaluate("""
            document.querySelector('#firstName').style.border = '5px solid red'
        """)
        time.sleep(5)