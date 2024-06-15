from selenium import webdriver
from selenium.webdriver import Keys
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

# Sending keys to elements
driver.find_element(By.XPATH, "//input[@id='search']").send_keys("Apple iPhone")

# Clearing the Textbox and again sending the keys to textbox
driver.find_element(By.XPATH, "//input[@id='search']").clear()

# If above not worked
driver.find_element(By.XPATH, "//input[@id='search']").send_keys(Keys.CONTROL + "A")
driver.find_element(By.XPATH, "//input[@id='search']").send_keys(Keys.BACKSPACE)
time.sleep(3)

driver.find_element(By.XPATH, "//input[@id='search']").send_keys("Apple iPhone")
time.sleep(5)
