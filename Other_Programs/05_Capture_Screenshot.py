from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

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
time.sleep(3)

# Capture a screenshot of the page
driver.save_screenshot('screenshot_example.png')
print("Screenshot of Example page saved as screenshot_example.png")
time.sleep(2)
