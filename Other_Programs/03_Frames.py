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
driver.get('https://demo.automationtesting.in/Frames.html')
driver.maximize_window()
time.sleep(3)

# # If You normally pass this directly it will give error
# driver.find_element(By.XPATH, "(//input) [1]").send_keys("Python")


# For this you have to 1st switch to this frame then only you will be able to enter the text
driver.switch_to.frame("singleframe")
driver.find_element(By.XPATH, "(//input) [1]").send_keys("Python")
time.sleep(3)
