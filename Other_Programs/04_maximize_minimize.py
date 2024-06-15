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

# For Maximizing browser window
driver.maximize_window()
time.sleep(3)

# For Minimizing browser window
driver.minimize_window()
time.sleep(3)

# For Full screen of window
driver.fullscreen_window()
time.sleep(3)
