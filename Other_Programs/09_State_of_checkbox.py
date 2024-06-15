from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
driver.get('https://only-testing-blog.blogspot.com/2014/01/textbox.html')
driver.maximize_window()
time.sleep(3)

Bike_Checkbox = driver.find_element(By.XPATH, "//input[@id='check1']")

# If we want checkbox as deselected, first we will check its condition, if it checked we will uncheck it and vice versa
is_checkbox_selected = Bike_Checkbox.is_selected()
print(f"Checkbox is selected: {is_checkbox_selected}")
if is_checkbox_selected == True:
    Bike_Checkbox.click()

time.sleep(3)

Car_Checkbox = driver.find_element(By.XPATH, "//input[@id='check2']")

# If we want checkbox as selected, first we will check its condition, if it unchecked we will uncheck it and vice versa
is_checkbox_selected = Car_Checkbox.is_selected()
print(f"Checkbox is selected: {is_checkbox_selected}")
if is_checkbox_selected == True:
    Car_Checkbox.click()

time.sleep(3)
