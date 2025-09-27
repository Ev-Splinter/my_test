from conftest import browser
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

button_selector = (By.CSS_SELECTOR, '#rosterBox > div:nth-child(5) > div > div:nth-child(2)')
result_selector = (By.CSS_SELECTOR, '#rosterBox > div:nth-child(7) > div > div.player-timeline-names > span:nth-child(7) > a')

class NaviRosterPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.hltv.org/team/4608/natus-vincere#tab-rosterBox')

    def button(self):
        return self.find(button_selector)

    def click_button(self):
        self.button().click()

    def result(self):
        return self.find(result_selector)

    def result_text(self):
        return self.result().text
