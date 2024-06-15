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
driver.get('https://only-testing-blog.blogspot.com/2014/01/textbox.html')
driver.maximize_window()
time.sleep(3)

# Select Dropdown_by_click:
Dropdown = driver.find_element(By.XPATH, "//select[@id='Carlist']")
Dropdown.click()

Dropdown_Option_Toyota = driver.find_element(By.XPATH, "//option[@id='car5']")
Dropdown_Option_Toyota.click()
Dropdown.click()
time.sleep(5)

# Select Dropdown_by_value:
select = Select(Dropdown)   # Storing value under select
select.select_by_value("BMW Car")
time.sleep(5)

# Select Dropdown_by_index:
select = Select(Dropdown)   # Storing value under select
select.select_by_index(3)
time.sleep(5)

# Select Dropdown_by_visible_text:
select = Select(Dropdown)   # Storing value under select
select.select_by_visible_text("Renault")
time.sleep(5)
