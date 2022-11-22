import pytest
import selenium
from pages.home_page import HomePage
from pages.first_recommended_chanel_page import FirstRecommendedChanel


def test_pausing_stream(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.pausing_stream(driver)
    assert first_rec_chanel.show_pausing_message().is_displayed()


def test_muting_stream(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.muting_stream(driver)
    assert first_rec_chanel.stream_is_muted(driver) == 'Stream is muted!'


def test_change_video_quality_of_stream(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_settings_button(driver)
    first_rec_chanel.click_quality_button()
    first_rec_chanel.select_160p_quality()
    assert first_rec_chanel.quality_video_change_check(driver) == '160p'


def test_video_statistics(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_settings_button(driver)
    first_rec_chanel.click_advanced_button()
    first_rec_chanel.click_video_statistics_button()
    assert first_rec_chanel.check_video_statistics_window().is_displayed()


def test_mini_player_window(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_settings_button(driver)
    first_rec_chanel.click_advanced_button()
    first_rec_chanel.mini_player_activate()
    first_rec_chanel.click_view_button()
    assert first_rec_chanel.check_mini_player_window().is_displayed()


def test_report_a_bug_selection(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_settings_button(driver)
    first_rec_chanel.click_report_a_bug()
    first_rec_chanel.select_a_bug()
    assert first_rec_chanel.error_option_selected().is_selected()


def test_show_hotkeys_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_settings_button(driver)
    first_rec_chanel.click_show_hotkeys()
    assert first_rec_chanel.list_of_hotkeys().is_displayed()


def test_theatre_mode_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_theatre_mode_button(driver)
    assert first_rec_chanel.theatre_mode_activated() is True


def test_full_screen_mode_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_full_screen_button(driver)
    assert first_rec_chanel.full_screen_mode_activated() is True


def test_write_message_to_chat(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.open_chat()
    first_rec_chanel.write_message_to_chat()
    assert first_rec_chanel.message_to_chat() == 'Всем привет, хорошего настроения!'
