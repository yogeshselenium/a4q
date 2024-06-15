# test_cases.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from Locators import GooglePageLocators
from Resources import WebDriverSetup


def test_google_search():
    # Initialize the WebDriver
    driver = WebDriverSetup.get_webdriver()

    try:
        # Open Google
        driver.get("https://www.google.com")

        # Accept cookies if the prompt appears (depends on region and browser state)
        time.sleep(2)
        try:
            accept_cookies_button = driver.find_element(By.XPATH, "//div[contains(text(), 'I agree')]")
            accept_cookies_button.click()
        except:
            pass

        # Find the search box and enter the search term
        search_box = driver.find_element(By.NAME, GooglePageLocators.SEARCH_BOX)
        search_box.send_keys("Selenium WebDriver")
        search_box.send_keys(Keys.RETURN)

        # Wait for the results to load
        time.sleep(3)

        # Verify search results page loaded
        assert "Selenium WebDriver" in driver.title
        print("Test Passed: Google search executed successfully.")

    finally:
        # Close the WebDriver
        driver.quit()


# Execute the test
if __name__ == "__main__":
    test_google_search()
