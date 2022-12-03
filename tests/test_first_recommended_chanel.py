from pages.home_page import HomePage
from pages.first_recommended_chanel_page import FirstRecommendedChanel
import pytest
import allure


@allure.feature('First recommended channel')
@allure.story('Pausing stream')
@allure.title('Testing pausing stream')
def test_pausing_stream(driver):
    home_page = HomePage(driver)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Click first recommended channel'):
        home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    with allure.step('Pausing stream'):
        first_rec_chanel.pausing_stream(driver)
    with allure.step('Check that the pause button changes to the play button'):
        assert first_rec_chanel.show_pausing_message().is_displayed()


@allure.feature('First recommended channel')
@allure.story('Muting stream')
@allure.title('Testing muting stream')
def test_muting_stream(driver):
    home_page = HomePage(driver)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Click first recommended channel'):
        home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    with allure.step('Muting stream'):
        first_rec_chanel.muting_stream(driver)
    with allure.step('Check that mute changed to unmute'):
        assert first_rec_chanel.stream_is_muted(driver) == 'Stream is muted!'


@allure.feature('First recommended channel')
@allure.story('Changing quality of video')
@allure.title('Testing changing quality of video')
def test_change_video_quality_of_stream(driver):
    home_page = HomePage(driver)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Click first recommended channel'):
        home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    with allure.step('Click settings button'):
        first_rec_chanel.click_settings_button(driver)
    with allure.step('Click quality button'):
        first_rec_chanel.click_quality_button()
    with allure.step('Select 160p quality'):
        first_rec_chanel.select_160p_quality()
    with allure.step('Check that quality of video is 160p'):
        assert first_rec_chanel.quality_video_change_check(driver) == '160p'


@allure.feature('First recommended channel')
@allure.story('Show video statistics')
@allure.title('Testing video statistics button')
def test_video_statistics(driver):
    home_page = HomePage(driver)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Click first recommended channel'):
        home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    with allure.step('Click settings button'):
        first_rec_chanel.click_settings_button(driver)
    with allure.step('Click advanced button'):
        first_rec_chanel.click_advanced_button()
    with allure.step('Click video statistics button'):
        first_rec_chanel.click_video_statistics_button()
    with allure.step('Check that video statistics window is displayed'):
        assert first_rec_chanel.check_video_statistics_window().is_displayed()


@allure.feature('First recommended channel')
@allure.story('Switch to mini player of stream')
@allure.title('Testing mini player mod')
def test_mini_player_window(driver):
    home_page = HomePage(driver)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Click first recommended channel'):
        home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    with allure.step('Click settings button'):
        first_rec_chanel.click_settings_button(driver)
    with allure.step('Click advanced button'):
        first_rec_chanel.click_advanced_button()
    with allure.step('Click mini player activate button'):
        first_rec_chanel.mini_player_activate()
    with allure.step('Go to view page'):
        first_rec_chanel.click_view_button()
    with allure.step('Check that the stream continued in the mini player'):
        assert first_rec_chanel.check_mini_player_window().is_displayed()


@allure.feature('First recommended channel')
@allure.story('Report a bug')
@allure.title('Testing report a bug button')
def test_report_a_bug_selection(driver):
    home_page = HomePage(driver)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Click first recommended channel'):
        home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    with allure.step('Click settings button'):
        first_rec_chanel.click_settings_button(driver)
    with allure.step('Click report a bug button'):
        first_rec_chanel.click_report_a_bug()
    with allure.step('Select a bug'):
        first_rec_chanel.select_a_bug()
    with allure.step('Check that first reason is select'):
        assert first_rec_chanel.error_option_selected().is_selected()


@allure.feature('First recommended channel')
@allure.story('Show hotkeys')
@allure.title('Testing show hotkeys button')
def test_show_hotkeys_button(driver):
    home_page = HomePage(driver)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Click first recommended channel'):
        home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    with allure.step('Click settings button'):
        first_rec_chanel.click_settings_button(driver)
    with allure.step('Click show hotkeys'):
        first_rec_chanel.click_show_hotkeys()
    with allure.step('Check that hotkeys window is displayed'):
        assert first_rec_chanel.list_of_hotkeys().is_displayed()


@allure.feature('First recommended channel')
@allure.story('Theatre mod')
@allure.title('Testing theatre mode button')
def test_theatre_mode_button(driver):
    home_page = HomePage(driver)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Click first recommended channel'):
        home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    with allure.step('Click theatre mode button'):
        first_rec_chanel.click_theatre_mode_button(driver)
    with allure.step('Check that video plays on theatre mode'):
        assert first_rec_chanel.theatre_mode_activated() is True


@allure.feature('First recommended channel')
@allure.story('Full screen mod')
@allure.title('Testing full screen button')
def test_full_screen_mode_button(driver):
    home_page = HomePage(driver)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Click first recommended channel'):
        home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    with allure.step('Click full screen button'):
        first_rec_chanel.click_full_screen_button(driver)
    with allure.step('Check that video plays on full screen mode'):
        assert first_rec_chanel.full_screen_mode_activated() is True


@allure.feature('First recommended channel')
@allure.story('Send message to chat')
@allure.title('Testing sending message to chat')
def test_message_to_chat_without_signin_not_working(driver):
    home_page = HomePage(driver)
    with allure.step('Open Home page'):
        home_page.open_page()
    with allure.step('Click first recommended channel'):
        home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    with allure.step('Open chat'):
        first_rec_chanel.open_chat()
    with allure.step('Write message to chat'):
        first_rec_chanel.write_message_to_chat()
    with allure.step('Check that join to twitch window is displayed'):
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
def test_searching_field(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.find_dreadztv_chanel()
    assert first_rec_chanel.dreadztv_chanel().is_displayed()


# 27
def test_collapse_recommended_channels(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_collapse_recommended_channels()
    assert first_rec_chanel.only_icons_of_streams().is_displayed()


# 28
def test_show_more_channels_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_show_more_channels_button()
    assert first_rec_chanel.more_channels().is_displayed()


# 29
def test_dark_mode_toggle(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_user_menu_toggle()
    first_rec_chanel.activate_dark_mode_toggle()
    assert first_rec_chanel.dark_mode().is_enabled()


# 30
def test_change_language(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_user_menu_toggle()
    first_rec_chanel.click_language_button()
    first_rec_chanel.chose_english_language()
    assert first_rec_chanel.navigation_in_english().is_displayed()


# 31
def test_logout_button(driver):
    home_page = HomePage(driver)
    home_page.open_page()
    home_page.click_first_recommended_chanel()
    first_rec_chanel = FirstRecommendedChanel(driver)
    first_rec_chanel.click_user_menu_toggle()
    first_rec_chanel.click_logout_button()
    assert first_rec_chanel.sign_in_window().is_displayed()
