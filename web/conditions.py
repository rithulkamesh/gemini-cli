from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MessageGenerationComplete(object):
    def __init__(self, locator, timeout=30):
        self.locator = locator
        self.timeout = timeout

    def __call__(self, driver):
        element = driver.find_element(*self.locator)

        def is_generation_complete(driver):
            script = """
                const element = arguments[0];
                const observer = new MutationObserver(function(mutations) {
                    mutations.forEach(function(mutation) {
                        if (mutation.addedNodes.length || mutation.removedNodes.length) {
                            window.generation_complete = false;
                        }
                    });
                });

                observer.observe(element, { childList: true, subtree: true });

                setTimeout(function() {
                    window.generation_complete = true;
                    observer.disconnect();
                }, 500);

                return window.generation_complete;
            """
            return driver.execute_script(script, element)

        try:
            WebDriverWait(driver, self.timeout).until(is_generation_complete)
            return element
        except:
            return False
