from pages.base_page import BasePage
from pages.locators import first_recommended_chanel_locators as apl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


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
        ActionChains(driver).move_to_element(self.find_element(
            apl.stream_screen)).click(self.find_element(apl.settings_button)).perform()

    def click_quality_button(self):
        self.find_element(apl.quality_video_button).click()

    def select_160p_quality(self):
        field_of_settings_by_video_qualities = self.find_element(apl.field_of_settings)
        list_of_qualities = field_of_settings_by_video_qualities.find_elements(
            By.CSS_SELECTOR, 'div[class="Layout-sc-1xcs6mc-0 beAYWq"]')
        list_of_qualities[6].click()

    def quality_video_change_check(self, driver):
        ActionChains(driver).move_to_element(self.find_element(apl.stream_screen)).click(
            self.find_element(apl.settings_button)).perform()
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

    def click_report_a_bug(self):
        self.find_element(apl.report_a_bug_button).click()

    def select_a_bug(self):
        self.select_by_text(apl.select_report)

    def error_option_selected(self):
        return self.find_element(apl.first_report)

    def click_show_hotkeys(self):
        settings_menu_field = self.find_element(apl.settings_menu_field)
        settings_buttons = settings_menu_field.find_elements(
            By.CSS_SELECTOR, 'div[class="Layout-sc-1xcs6mc-0 hUemkh"]')
        hotkeys_button = settings_buttons[5]
        hotkeys_button.click()

    def list_of_hotkeys(self):
        return self.find_element(apl.list_of_hotkeys)

    def click_theatre_mode_button(self, driver):
        self.start_watching()
        ActionChains(driver).move_to_element(self.find_element(apl.stream_screen)).click(
            self.find_element(apl.theatre_mode_button)).perform()

    def theatre_mode_activated(self):
        return self.find_element(apl.check_theatre_mode).is_displayed()

    def click_full_screen_button(self, driver):
        self.start_watching()
        full_screen_button = self.find_elements(apl.full_screen_button)
        ActionChains(driver).move_to_element(self.find_element(apl.stream_screen)).click(
            full_screen_button[0]).perform()

    def full_screen_mode_activated(self):
        return self.find_element(apl.check_fullscreen_mode).is_displayed()

    def open_chat(self):
        if self.find_element(apl.close_chat_button).is_displayed():
            pass
        else:
            self.find_element(apl.open_chat_button).click()

    def write_message_to_chat(self):
        message = self.find_element(apl.message_to_chat_field)
        message.send_keys('Всем привет, хорошего настроения!')
        message.send_keys(Keys.ENTER)

    def join_to_twitch_window(self):
        return self.find_element(apl.join_to_twitch_window)

    def click_community_button(self):
        self.find_element(apl.community_button).click()

    def info_about_community(self):
        return self.find_element(apl.filter_field)

    def click_chat_settings_button(self):
        self.find_element(apl.chat_settings_button).click()

    def enable_chat_filtration(self):
        self.find_element(apl.chat_filter_button).click()
        self.find_element(apl.enable_filtration_in_chat).click()

    def chat_filtration(self):
        return self.find_element(apl.enable_filtration_in_chat)

    def click_community_points_button(self):
        self.find_element(apl.community_points_button).click()

    def channel_points_reward(self):
        return self.find_element(apl.channel_points_reward)

    def click_chat_send_button(self):
        self.find_element(apl.chat_send_button).click()

    def click_follow_button(self):
        self.find_element(apl.follow_button).click()

    def click_subscribe_button(self):
        self.find_element(apl.subscribe_button).click()

    def subscription_info(self):
        return self.find_element(apl.subscription_info)

    def click_paid_subscription(self):
        self.find_element(apl.subscribe_main_button).click()

    def sign_in_window(self):
        return self.find_element(apl.sing_in_window)

    def click_donate_subscription(self):
        donate_a_subscription_field = self.find_element(apl.donate_a_subscription_field)
        donate_a_subscription_field.find_element(By.CLASS_NAME, 'hUInuk').click()

    def gift_for_community_window(self):
        return self.find_element(apl.gift_for_community_window)

    def click_show_love_gift_theme(self):
        self.find_element(apl.show_love_button).click()

    def show_love_gif(self):
        return self.find_element(apl.show_love_gif)

    def click_party_gift_theme(self):
        self.find_element(apl.party_button).click()

    def party_gif(self):
        return self.find_element(apl.party_gif)

    def click_lul_gift_theme(self):
        self.find_element(apl.lul_button).click()

    def lul_gif(self):
        return self.find_element(apl.lul_gif)

    def click_biblethump_gift_theme(self):
        self.find_element(apl.biblethump_button).click()

    def biblethump_gif(self):
        return self.find_element(apl.biblethump_gif)

    def click_share_button(self):
        self.find_element(apl.share_button).click()

    def share_with_field(self):
        return self.find_element(apl.share_field)

    def click_report_button(self):
        self.find_element(apl.report_button).click()

    def click_report_translation_button(self):
        self.find_element(apl.report_translation_button).click()

    def click_report_other_button(self):
        self.find_element(apl.report_other_button).click()

    def pause_chat_by_scroll(self, driver):
        scroll_origin = ScrollOrigin.from_viewport(10, 10)
        ActionChains(driver).move_to_element(
            self.find_element(apl.chat_scroller)).scroll_from_origin(scroll_origin, 0, -50).perform()
        sleep(9)
