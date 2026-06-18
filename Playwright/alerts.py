import time

import pytest
from playwright.sync_api import sync_playwright, expect

SUPPORTED_BROWSERS = ["chromium", "firefox", "edge"]
BROWSER_NAME = "chromium"
HEADLESS = False
URL = "https://automation.ebrahimhossain.com.bd/hovers.html"
ALERT_URL= "https://automation.ebrahimhossain.com.bd/alerts.html"


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
    page.goto(ALERT_URL)
    request.cls.page = page

    yield

    context.close()
    browser.close()
    playwright.stop()

@pytest.mark.usefixtures("setup")
class TestAlertsExample :
    def test_alertsexample1(self):

        def handle_alert(dialog):
            print("Type : ", dialog.type)
            print("Message", dialog.message)
            dialog.accept()


        self.page.once("dialog", handle_alert)

        triger = self.page.locator("#alertBtn")
        triger.click()
        time.sleep(1)


    def test_alertsexample2(self):

        def handle_alert(dialog):
            print("Type : ", dialog.type)
            print("Message", dialog.message)
            dialog.dismiss()


        self.page.once("dialog", handle_alert)

        triger = self.page.locator("#confirmBtn")
        triger.click()
        time.sleep(1)

    def test_alertsexample3(self):

        def handle_alert(dialog):
            print("Type : ", dialog.type)
            print("Message", dialog.message)
            dialog.accept()


        self.page.once("dialog", handle_alert)

        triger = self.page.locator("#promptBtn")
        triger.click()
        time.sleep(1)

    def test_alertsexample4(self):
        def handle_alert(dialog):
            print("Type : ", dialog.type)
            print("Message", dialog.message)
            dialog.accept()

        self.page.once("dialog", handle_alert)

        triger = self.page.locator("#promptBtn")
        triger.click()
        time.sleep(1)

    def test_alertToaste1(self):
        toaster_btn = self.page.locator("(//button[contains(@class,'action-btn btn-secondary')])[1]")
        toaster_btn.click()
        time.sleep(1)
        toaster_location = self.page.locator("[data-testid='toast-success-item']")
        expect(toaster_location).to_contain_text("Success! Record updated.")
        time.sleep(2)

    def test_alertToaste2(self):
        toaster_btn = self.page.locator("[data-testid='toast-info-btn']")
        toaster_btn.click()
        time.sleep(1)
        toast_success = self.page.locator("[data-testid='toast-info-item']")
        expect(toast_success).to_contain_text("System will restart in 5 minutes.")
        time.sleep(6)
        expect(toast_success).not_to_be_visible(timeout=5)












