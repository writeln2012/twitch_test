from pages.base_page import BasePage
from pages.locators import first_recommended_chanel_locators as apl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


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

    def click_settings_button(self, driver):
        self.start_watching()
        ActionChains(driver).move_to_element(self.find_element(apl.stream_screen)).click(self.find_element(
            apl.settings_button)).perform()

    def click_quality_button(self):
        self.find_element(apl.quality_video_button).click()

    def select_160p_quality(self):
        field_of_settings_by_video_qualities = self.find_element(apl.field_of_settings)
        list_of_qualities = field_of_settings_by_video_qualities.find_elements(
            By.CSS_SELECTOR, 'div[class="Layout-sc-1xcs6mc-0 beAYWq"]')
        list_of_qualities[6].click()

    def quality_video_change_check(self, driver):
        ActionChains(driver).move_to_element(self.find_element(apl.stream_screen)).click(self.find_element(
            apl.settings_button)).perform()
        check_quality = self.find_element(apl.quality_video_check)
        return check_quality.text

    def click_advanced_button(self):
        self.find_element(apl.advanced_button).click()

    def click_video_statistics_button(self):
        advanced_settings_field = self.find_element(apl.advanced_settings_field)
        advanced_settings = advanced_settings_field.find_elements(
            By.CSS_SELECTOR, 'div[class="Layout-sc-1xcs6mc-0 jwovJQ"')
        video_statistics = advanced_settings[2]
        video_statistics.click()

    def check_video_statistics_window(self):
        return self.find_element(apl.video_statistics_window)

    def mini_player_activate(self):
        indicator_of_mini_player = self.find_element(apl.indicator_of_mini_player)
        if indicator_of_mini_player.is_enabled():
            pass
        else:
            indicator_of_mini_player.click()

    def click_view_button(self):
        self.find_element(apl.view_button).click()

    def check_mini_player_window(self):
        return self.find_element(apl.mini_player_window)
