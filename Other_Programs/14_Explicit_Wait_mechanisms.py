from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Specify the path to your WebDriver
driver_path = "C://Program Files//Python310//Scripts//chromedriver.exe"

# Create a Service object with the path to the WebDriver
service = Service(driver_path)

# Create an Options object
options = Options()

# Initialize the WebDriver (Chrome in this example)
driver = webdriver.Chrome(service=service, options=options)

# Open the website
driver.get('https://magento.softwaretestingboard.com/')
driver.maximize_window()
time.sleep(5)

# Explicit Wait

# Explicit wait Declaration
wait = WebDriverWait(driver, 10)

# This is explicit waits
clickable_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Shop New Yoga')]")))

# Now click the element
clickable_element.click()

time.sleep(5)
