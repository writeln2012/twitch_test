from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = 'https://www.twitch.tv/'

    def find_element(self, args: tuple):
        by_name, by_val = args
        return self.driver.find_element(by_name, by_val)

    def find_elements(self, args: tuple):
        by_name, by_val = args
        return self.driver.find_elements(by_name, by_val)

    def scroll_page_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def select_by_text(self, args: tuple):
        by_name, by_val, text = args
        Select(self.driver.find_element(by_name, by_val)).select_by_visible_text(text)

    def select_by_value(self, args: tuple):
        by_name, by_val, value = args
        Select(self.driver.find_element(by_name, by_val)).select_by_value(value)

    def start_watching(self):
        try:
            self.driver.find_element(By.CSS_SELECTOR, 'button[data-a-target="player-overlay-mature-accept"]').click()

        except NoSuchElementException:
            pass

        else:
            pass
