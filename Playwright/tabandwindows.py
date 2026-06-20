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
       new_tab3.close()
       time.sleep(2)
       new_tab2.close()
       new_tab1.close()
       time.sleep(2)


