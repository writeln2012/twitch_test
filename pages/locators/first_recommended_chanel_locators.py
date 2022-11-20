from selenium.webdriver.common.by import By


stream_screen = (By.CLASS_NAME, 'stream-display-ad__wrapper')
pause_play_button = (By.CSS_SELECTOR, 'button[data-a-target="player-play-pause-button"]')
pause_message = (By.CSS_SELECTOR, 'button[aria-label="Воспроизведение (пробел/k)"]')
start_watching = (By.CSS_SELECTOR, 'button[data-a-target="player-overlay-mature-accept"]')
mute_button = (By.CSS_SELECTOR, 'button[aria-label="Выкл. звук (m)"]')
settings_button = (By.CSS_SELECTOR, 'button[data-a-target="player-settings-button"]')
quality_video_button = (By.CSS_SELECTOR, 'button[data-a-target="player-settings-menu-item-quality"]')
field_of_settings = (By.CSS_SELECTOR, 'div[data-a-target="player-settings-menu"]')
list_of_video_qualities = (By.CSS_SELECTOR, 'div[class="Layout-sc-1xcs6mc-0 beAYWq"]')
quality_video_check = (By.CLASS_NAME, 'kLZqyf')
advanced_button = (By.CSS_SELECTOR, 'button[data-a-target="player-settings-menu-item-advanced"]')
advanced_settings_field = (By.CSS_SELECTOR, 'div[data-a-target="player-settings-menu"]')
video_statistics_window = (By.CSS_SELECTOR, 'div[data-a-target="player-overlay-video-stats"]')
indicator_of_mini_player = (By.CSS_SELECTOR, 'div[data-a-target="player-settings-submenu-advanced-toggle-mini"]')
view_button = (By.CLASS_NAME, 'navigation-link')
mini_player_window = (By.CLASS_NAME, 'video-player__overlay')
report_a_bug_button = (By.CSS_SELECTOR, 'button[data-a-target="player-settings-menu-item-report"]')
select_report = (
    By.CSS_SELECTOR, 'select[class="ScInputBase-sc-vu7u7d-0 ScSelect-sc-gz38t2-0'
                     ' gXVFsI AJDRH InjectLayout-sc-1i43xsx-0 bLZRbT tw-select"]', '«Заикание» звука и изображения')
first_report = (By.CSS_SELECTOR, 'option[value="stutter-both"]')
settings_menu_field = (By.CSS_SELECTOR, 'div[data-a-target="player-settings-menu"]')
list_of_hotkeys = (By.CLASS_NAME, 'tw-table-body')
