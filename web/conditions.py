from selenium.common.exceptions import TimeoutException
import time


class WaitUntilContentLoads:
    def __init__(self, locator, timeout=30, stability_time=3):
        """
        :param locator: Locator for the content container.
        :param timeout: How long to wait in total (seconds).
        :param stability_time: How long the DOM should stay unchanged to assume loading is done (seconds).
        """
        self.locator = locator
        self.timeout = timeout
        self.stability_time = stability_time

    def __call__(self, driver):
        end_time = time.time() + self.timeout
        last_snapshot = None
        stable_since = None

        while time.time() < end_time:
            try:
                element = driver.find_element(*self.locator)
                current_snapshot = element.get_attribute('innerHTML')

                if current_snapshot == last_snapshot:
                    # If the DOM hasn't changed, check if it's been stable long enough
                    if stable_since is None:
                        stable_since = time.time()  # Start the stability timer
                    elif time.time() - stable_since >= self.stability_time:
                        return True  # DOM is stable
                else:
                    last_snapshot = current_snapshot
                    stable_since = None  # Reset the timer if the DOM has changed

                # Wait a bit before checking again
                time.sleep(1)
            except:
                # If there's an error (e.g., element not found), retry after a short pause.
                time.sleep(1)
                continue

        raise TimeoutException(
            "The DOM did not stabilize within the allotted time.")
