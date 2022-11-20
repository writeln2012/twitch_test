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
