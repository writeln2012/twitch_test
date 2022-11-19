from pages.base_page import BasePage
from pages.locators import first_recommended_chanel_locators as apl
from selenium.webdriver.common.action_chains import ActionChains


class FirstRecommendedChanel(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def pausing_stream(self, driver):
        start_watching_button = self.find_element(apl.start_watching)
        if start_watching_button.is_displayed():
            start_watching_button.click()
            ActionChains(driver).move_to_element(self.find_element(apl.stream_screen)).click(
                self.find_element(apl.pause_play_button)).perform()
        else:
            ActionChains(driver).move_to_element(self.find_element(apl.stream_screen)).click(
                self.find_element(apl.pause_play_button)).perform()

    def show_pausing_message(self):
        pause_message = self.find_element(apl.pause_message)
        return pause_message
