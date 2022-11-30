import pytest
import selenium
from pages.home_page import HomePage
from pages.first_recommended_chanel_page import FirstRecommendedChanel


# 1
def test_pausing_stream(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.pausing_stream(driver)
    assert first_rec_chanel.show_pausing_message().is_displayed()


# 2
def test_muting_stream(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.muting_stream(driver)
    assert first_rec_chanel.stream_is_muted(driver) == 'Stream is muted!'


# 3
def test_change_video_quality_of_stream(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_settings_button(driver)
    first_rec_chanel.click_quality_button()
    first_rec_chanel.select_160p_quality()
    assert first_rec_chanel.quality_video_change_check(driver) == '160p'


# 4
def test_video_statistics(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_settings_button(driver)
    first_rec_chanel.click_advanced_button()
    first_rec_chanel.click_video_statistics_button()
    assert first_rec_chanel.check_video_statistics_window().is_displayed()


# 5
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


# 6
def test_report_a_bug_selection(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_settings_button(driver)
    first_rec_chanel.click_report_a_bug()
    first_rec_chanel.select_a_bug()
    assert first_rec_chanel.error_option_selected().is_selected()


# 7
def test_show_hotkeys_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_settings_button(driver)
    first_rec_chanel.click_show_hotkeys()
    assert first_rec_chanel.list_of_hotkeys().is_displayed()


# 8
def test_theatre_mode_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_theatre_mode_button(driver)
    assert first_rec_chanel.theatre_mode_activated() is True


# 9
def test_full_screen_mode_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_full_screen_button(driver)
    assert first_rec_chanel.full_screen_mode_activated() is True


# 10
def test_message_to_chat_without_signin_not_working(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.open_chat()
    first_rec_chanel.write_message_to_chat()
    assert first_rec_chanel.join_to_twitch_window().is_displayed()


# 11
def test_community_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.open_chat()
    first_rec_chanel.click_community_button()
    assert first_rec_chanel.info_about_community().is_displayed()


# 12
def test_chat_filtration_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.open_chat()
    first_rec_chanel.click_chat_settings_button()
    first_rec_chanel.enable_chat_filtration()
    assert first_rec_chanel.chat_filtration().is_enabled()


# 13
def test_community_points_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.open_chat()
    first_rec_chanel.click_community_points_button()
    assert first_rec_chanel.channel_points_reward().is_displayed()


# 14
def test_chat_send_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.open_chat()
    first_rec_chanel.click_chat_send_button()
    assert first_rec_chanel.join_to_twitch_window().is_displayed()


# 15
def test_follow_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_follow_button()
    assert first_rec_chanel.join_to_twitch_window().is_displayed()


# 16
def test_subscribe_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_subscribe_button()
    assert first_rec_chanel.subscription_info().is_displayed()


# 17
def test_paid_subscribe_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_subscribe_button()
    first_rec_chanel.click_paid_subscription()
    assert first_rec_chanel.sign_in_window().is_displayed()


# 18
def test_donate_subscription_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_subscribe_button()
    first_rec_chanel.click_donate_subscription()
    assert first_rec_chanel.gift_for_community_window().is_displayed()


# 19
def test_show_love_gif_in_gift_theme(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_subscribe_button()
    first_rec_chanel.click_donate_subscription()
    first_rec_chanel.click_show_love_gift_theme()
    assert first_rec_chanel.show_love_gif().is_displayed()


# 20
def test_party_gif_in_gift_theme(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_subscribe_button()
    first_rec_chanel.click_donate_subscription()
    first_rec_chanel.click_party_gift_theme()
    assert first_rec_chanel.party_gif().is_displayed()


# 21
def test_lul_gif_in_gift_theme(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_subscribe_button()
    first_rec_chanel.click_donate_subscription()
    first_rec_chanel.click_lul_gift_theme()
    assert first_rec_chanel.lul_gif().is_displayed()


# 22
def test_biblethump_gif_in_gift_theme(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_subscribe_button()
    first_rec_chanel.click_donate_subscription()
    first_rec_chanel.click_biblethump_gift_theme()
    assert first_rec_chanel.biblethump_gif().is_displayed()


# 23
def test_share_with_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_share_button()
    assert first_rec_chanel.share_with_field().is_displayed()


# 24
def test_report_translation_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_report_button()
    first_rec_chanel.click_report_translation_button()
    assert first_rec_chanel.sign_in_window().is_displayed()


# 25
def test_report_other_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_report_button()
    first_rec_chanel.click_report_other_button()
    assert first_rec_chanel.sign_in_window()


# 26
def test_streamers_icon(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_streamers_icon()
    assert first_rec_chanel.streamers_channel().is_displayed()



