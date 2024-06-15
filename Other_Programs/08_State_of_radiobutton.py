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
driver.get('https://only-testing-blog.blogspot.com/2014/01/textbox.html')
driver.maximize_window()
time.sleep(3)

# Locate a checkbox element
radiobutton = driver.find_element(By.XPATH, "//input[@id='radio1']")  # replace 'checkbox_id' with the actual ID

# Check if the checkbox is selected
is_checkbox_selected = radiobutton.is_selected()
print(f"Checkbox is selected: {is_checkbox_selected}")

# Checking the radio button
radiobutton.click()

# Check if the checkbox is selected
is_checkbox_selected = radiobutton.is_selected()
print(f"Checkbox is selected: {is_checkbox_selected}")

time.sleep(3)
