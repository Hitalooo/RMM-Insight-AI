from playwright.sync_api import sync_playwright


class DattoBrowser:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None


    def start(self, headless=False):

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=headless
        )

        self.page = self.browser.new_page()

        return self.page


    def close(self):

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()