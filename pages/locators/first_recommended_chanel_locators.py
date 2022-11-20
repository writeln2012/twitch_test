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
