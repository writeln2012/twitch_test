from pages.base_page import BasePage
from pages.locators import home_page_locators as apl


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.base_url)

    def click_first_recommended_chanel(self):
        self.find_element(apl.first_recommended_channel).click()
