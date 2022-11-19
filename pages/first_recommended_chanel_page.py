from pages.base_page import BasePage
from pages.locators import first_recommended_chanel_locators as apl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


class FirstRecommendedChanel(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def pausing_stream(self, driver):
        self.start_watching()
        ActionChains(driver).move_to_element(self.find_element(apl.stream_screen)).click(
                self.find_element(apl.pause_play_button)).perform()

    def show_pausing_message(self):
        pause_message = self.find_element(apl.pause_message)
        return pause_message

    def muting_stream(self, driver):
        self.start_watching()
        ActionChains(driver).move_to_element(self.find_element(apl.stream_screen)).click(
            self.find_element(apl.mute_button)).perform()

    def stream_is_muted(self, driver):
        try:
            ActionChains(driver).move_to_element(self.find_element(
                apl.stream_screen)).click(self.find_element(apl.mute_button)).perform()
        except NoSuchElementException:
            return 'Stream is muted!'
