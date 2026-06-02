import time
import pytest
from playwright.sync_api import sync_playwright

#Step 1: Choose Browser / Supported browser
SUPPORTED_BROWSERS = ["chromium", "firefox", "webkit"]
# Step 2: Define the browser
BROWSER_NAME = "chromium"
#Step 3: URL
URL = "https://google.com"

#Step 4: Setup + Teardown
@pytest.fixture(scope="class")
def setup(request):
    print(f"Starting {BROWSER_NAME} browser....")
    # Step 5: Start Playwright
    playwright = sync_playwright().start()
    #Step 6: Launch the browser
    if BROWSER_NAME == "chromium":
        browser = playwright.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"],
        )
    elif BROWSER_NAME == "firefox":
        browser = playwright.firefox.launch(headless=False)
    elif BROWSER_NAME == "webkit":
        browser = playwright.webkit.launch(headless=False)
    else:
        raise ValueError(f"Browser {BROWSER_NAME} is not supported.")
    # Step 7: create browser context / New Window
    context = browser.new_context()
    #Step 8: Create a new page / Tab
    page = context.new_page()
    # Viewport - Screen Size
    page.set_viewport_size({"width": 1920, "height": 1080})
    #Step 9: Open the URL
    page.goto(URL)

    request.cls.browser = browser
    request.cls.context = context
    request.cls.page = page
    request.cls.playwright = playwright

    # YIELD = Tests Run Here.....
    yield
    # Teardown
    context.close()
    browser.close()
    playwright.stop()

@pytest.mark.usefixtures("setup")
class TestTabAndWindow:
    def test_open_new_tab(self):
        new_tab = self.context.new_page()
        new_tab.goto("http://google.com")
        time.sleep(2)
        new_tab.close()

    def test_open_multiple_tabs(self):
        new_tab1 = self.context.new_page()
        new_tab2 = self.context.new_page()
        new_tab3 = self.context.new_page()
        new_tab1.goto("http://github.com")
        new_tab2.goto("http://youtube.com")
        new_tab3.goto("http://facebook.com")
        time.sleep(2)
        new_tab1.close()
        new_tab2.close()
        new_tab3.close()

    def test_switch_tab(self):
        new_tab1 = self.context.new_page()
        new_tab2 = self.context.new_page()
        new_tab3 = self.context.new_page()
        new_tab1.goto("http://github.com")
        new_tab2.goto("http://youtube.com")
        new_tab3.goto("http://facebook.com")
        time.sleep(2)

        new_tab1.bring_to_front()
        time.sleep(2)

        new_tab2.bring_to_front()
        time.sleep(2)

        new_tab1.bring_to_front()
        time.sleep(2)

        new_tab3.bring_to_front()
        time.sleep(2)

        new_tab1.close()
        new_tab2.close()
        new_tab3.close()

    def test_open_new_window(self):
        window = self.browser.new_context()
        new_page = window.new_page()
        new_page.goto("http://google.com")
        time.sleep(2)
        window.close()

    def test_open_multiple_window(self):
        window1 = self.browser.new_context()
        window2 = self.browser.new_context()
        window3 = self.browser.new_context()

        new_page1 = window1.new_page()
        new_page2 = window2.new_page()
        new_page3 = window3.new_page()
        new_page1.goto("http://github.com")
        time.sleep(2)
        new_page2.goto("http://youtube.com")
        time.sleep(2)
        new_page3.goto("http://facebook.com")
        time.sleep(2)


        window1.close()
        window2.close()
        window3.close()

    def test_custom_window_size(self):
        custom_browser = self.playwright.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled",
                  "--window-size=1200,900",
                  "--window-position=0,0"
                  ]
        )

        custom_context = custom_browser.new_context()
        custom_page = custom_context.new_page()
        custom_page.goto("http://google.com")
        time.sleep(2)

        custom_browser.close()