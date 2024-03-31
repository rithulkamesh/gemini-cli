from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc


def find_element(driver, selector):
    return WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    )


class Gemini:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.driver = uc.Chrome(
            headless=False, options=options, use_subprocess=False)

    def initialize(self, email: str, password: str):

        self.driver.get('https://gemini.google.com')

        sign_in_button = find_element(self.driver, '.gb_Ba')

        sign_in_button.click()

        email_input = find_element(self.driver, '#identifierId')
        email_input.send_keys(email)

        next_button = self.driver.find_element(
            By.CSS_SELECTOR, '#identifierNext')

        next_button.click()

        password_input = find_element(self.driver, 'input[type="password"]')
        password_input.send_keys(password)

        next_button = find_element(self.driver, '#passwordNext')
        next_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains('https://gemini.google.com/')
        )

        print("Logged into gemini successfully")

    def send_message(self, message: str):
        print("Sending message...")

        message_input = find_element(self.driver, '.ql-editor')
        message_input.send_keys(message)

        send_button = find_element(self.driver, '.send-button')
        send_button.click()

    def close(self):
        self.driver.quit()
        print("Browser closed")
