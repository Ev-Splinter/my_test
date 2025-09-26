from conftest import browser
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

button_selector = (By.CSS_SELECTOR, '[class="block button text-center"]')

class TeamsButtonPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.hltv.org/')

    def button(self):
        return self.find(button_selector)

