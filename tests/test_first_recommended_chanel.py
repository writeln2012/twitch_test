import pytest
from pages.home_page import HomePage
from pages.first_recommended_chanel_page import FirstRecommendedChanel


def test_pausing_stream(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.pausing_stream()
    assert first_rec_chanel.pausing_message().is_displayed()
