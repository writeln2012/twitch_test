from pages.base_page import BasePage
from pages.locators import first_recommended_chanel_locators as apl
from selenium.webdriver.common.action_chains import ActionChains


class FirstRecommendedChanel(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def pausing_stream(self):
        # ActionChains(self).move_to_element(self.find_element(apl.stream_screen)).click(self.find_element(apl.pause_play_button)).perform()
        stream_screen = self.find_element(apl.stream_screen)
        pause_play_button = self.find_element(apl.pause_play_button)
        ActionChains(self).move_to_element(stream_screen).click(pause_play_button).perform()

    def pausing_message(self):
        self.find_element(apl.pause_message)
