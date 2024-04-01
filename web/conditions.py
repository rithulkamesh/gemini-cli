from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MessageGenerationComplete(object):
    def __init__(self, locator, timeout=30, poll_frequency=1):
        self.locator = locator
        self.timeout = timeout
        self.poll_frequency = poll_frequency

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        prev_html = element.get_attribute("outerHTML")

        def check_message_generation(driver):
            nonlocal prev_html
            element = driver.find_element(*self.locator)
            current_html = element.get_attribute("outerHTML")
            if current_html != prev_html:
                prev_html = current_html
                return False
            else:
                return True

        try:
            WebDriverWait(driver, self.timeout, self.poll_frequency).until(
                check_message_generation)
            return element
        except:
            return False
