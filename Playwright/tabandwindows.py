import time

import pytest
from playwright.sync_api import sync_playwright, expect

SUPPORTED_BROWSERS = ["chromium", "firefox", "edge"]
BROWSER_NAME = "chromium"
HEADLESS = False
URL = "https://google.com"



@pytest.fixture(scope="class")
def setup (request):
    playwright =  sync_playwright().start()

    match BROWSER_NAME :
        case "chromium" :

            browser = playwright.chromium.launch(
                headless=False,
                args=["--disable-blink-features=AutomationControlled"],

            )
        case "firefox" :
            browser = playwright.firefox.launch(
                headless=False,
                args=["--disable-blink-features=AutomationControlled"],
            )
        case "edge" :
            browser = playwright.edge.launch(
                headless=False,
                args=["--disable-blink-features=AutomationControlled"],
            )
        case _:
            raise ValueError(f"Browser {BROWSER_NAME} is not supported.")


    context = browser.new_context()
    page = context.new_page()
    page.goto(URL)

    request.cls.playwright = playwright
    request.cls.browser = browser
    request.cls.context = context
    request.cls.page = page

    yield

    context.close()
    browser.close()
    playwright.stop()

@pytest.mark.usefixtures("setup")
class TestTabAndWindowExample :
    def test_open_new_tab(self):
       new_tab = self.context.new_page()
       new_tab.goto("https://portfolio-apurbokabbo.vercel.app/")
       time.sleep(4)
       new_tab.close()

    def test_open_multiple_tab(self):
       new_tab1 = self.context.new_page()
       new_tab2 = self.context.new_page()
       new_tab3 = self.context.new_page()
       new_tab1.goto("https://portfolio-apurbokabbo.vercel.app/")
       new_tab2.goto("http://youtube.com")
       time.sleep(2)
       new_tab3.goto("https://portfolio-apurbokabbo.vercel.app/")
       time.sleep(2)
       new_tab3.close()
       time.sleep(2)
       new_tab2.close()
       new_tab1.close()
       time.sleep(2)

    def test_open_multiple_tab_switch(self):
       new_tab1 = self.context.new_page()
       new_tab2 = self.context.new_page()
       new_tab3 = self.context.new_page()
       new_tab1.goto("https://portfolio-apurbokabbo.vercel.app/")
       new_tab2.goto("http://youtube.com")
       time.sleep(2)
       new_tab3.goto("https://portfolio-apurbokabbo.vercel.app/")
       time.sleep(2)
       new_tab2.bring_to_front()
       time.sleep(2)
       new_tab1.bring_to_front()
       time.sleep(2)
       new_tab3.bring_to_front()
       time.sleep(2)
       new_tab3.close()
       time.sleep(2)
       new_tab2.close()
       new_tab1.close()
       time.sleep(2)

    def test_open_new_window(self):
        # Create a new browser context (like a new window)
        new_context = self.browser.new_context()

        # Open a new page in this context
        new_page = new_context.new_page()

        # Navigate to the URL
        new_page.goto("https://portfolio-apurbokabbo.vercel.app/")

        # Optional wait
        time.sleep(4)

        # Close the context (which closes all pages in it)
        new_context.close()

    def test_open_multiple_window(self):
        # Create multiple browser contexts (like separate windows)
        new_context1 = self.browser.new_context()
        new_context2 = self.browser.new_context()
        new_context3 = self.browser.new_context()

        # Open new pages in each context
        new_tab1 = new_context1.new_page()
        new_tab2 = new_context2.new_page()
        new_tab3 = new_context3.new_page()

        # Navigate to URLs
        new_tab1.goto("https://portfolio-apurbokabbo.vercel.app/")
        new_tab2.goto("http://youtube.com")
        new_tab3.goto("https://portfolio-apurbokabbo.vercel.app/")

        # Optional: wait until page is loaded
        new_tab1.wait_for_load_state("domcontentloaded")
        new_tab2.wait_for_load_state("domcontentloaded")
        new_tab3.wait_for_load_state("domcontentloaded")

        # Close pages
        new_tab3.close()
        new_tab2.close()
        new_tab1.close()

        # Close contexts
        new_context1.close()
        new_context2.close()
        new_context3.close()

    def test_open_multiple_window_switch(self):
        # Create multiple browser contexts (like separate windows)
        new_context1 = self.browser.new_context()
        new_context2 = self.browser.new_context()
        new_context3 = self.browser.new_context()

        # Open new pages in each context
        new_tab1 = new_context1.new_page()
        new_tab2 = new_context2.new_page()
        new_tab3 = new_context3.new_page()

        # Navigate to URLs
        new_tab1.goto("https://portfolio-apurbokabbo.vercel.app/")
        new_tab2.goto("http://youtube.com")
        new_tab3.goto("https://portfolio-apurbokabbo.vercel.app/")

        # switch
        new_tab2.bring_to_front()
        time.sleep(2)
        new_tab1.bring_to_front()
        time.sleep(2)
        new_tab3.bring_to_front()
        time.sleep(2)

        # Optional: wait until page is loaded
        new_tab1.wait_for_load_state("domcontentloaded")
        new_tab2.wait_for_load_state("domcontentloaded")
        new_tab3.wait_for_load_state("domcontentloaded")

        # Close pages
        new_tab3.close()
        new_tab2.close()
        new_tab1.close()

        # Close contexts
        new_context1.close()
        new_context2.close()
        new_context3.close()

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



