from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc


class Gemini:
    def __init__(self, email, password):
        self.username = email
        self.password = password
        self.driver = None

    def initialize(self):
        print("Logging in to Gemini...")

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        self.driver = uc.Chrome(
            headless=False, options=options, use_subprocess=False)

        self.driver.get('https://gemini.google.com')

        # Click the sign-in button
        sign_in_button = self.driver.find_element(By.CSS_SELECTOR, '.gb_Ba')
        sign_in_button.click()

        # Wait for the Google sign-in page to load
        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '#identifierId'))
        )
        print("Google sign-in page loaded")

        # Fill in the Google sign-in credentials
        email_input.send_keys(self.username)
        next_button = self.driver.find_element(
            By.CSS_SELECTOR, '#identifierNext')
        next_button.click()
        print("Username filled successfully")

        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, 'input[type="password"]'))
        )
        print("Password page loaded")
        password_input.send_keys(self.password)
        next_button = self.driver.find_element(
            By.CSS_SELECTOR, '#passwordNext')
        next_button.click()

        # Wait for the Gemini page to load after successful sign-in
        WebDriverWait(self.driver, 10).until(
            EC.url_contains('https://gemini.google.com/')
        )
        print("Successfully logged in to Gemini")
