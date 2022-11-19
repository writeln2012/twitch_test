from selenium.webdriver.common.by import By


stream_screen = (By.CLASS_NAME, 'stream-display-ad__wrapper')
pause_play_button = (By.CSS_SELECTOR, 'button[data-a-target="player-play-pause-button"]')
pause_message = (By.CSS_SELECTOR, 'button[aria-label="Воспроизведение (пробел/k)"]')
start_watching = (By.CSS_SELECTOR, 'button[data-a-target="player-overlay-mature-accept"]')
