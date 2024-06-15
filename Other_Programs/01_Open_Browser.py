from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Specify the path to your WebDriver
#driver_path = "C://Program Files//Python310//Scripts//chromedriver.exe"
driver_path= "C://Users//suraj//AppData//Local//Programs//Python//Python312//Scripts//chromedriver.exe"
# Create a Service object with the path to the WebDriver
service = Service(driver_path)

# Create an Options object
options = Options()

# Initialize the WebDriver (Chrome in this example)
driver = webdriver.Chrome(service=service, options=options)

# Open the website
driver.get('https://magento.softwaretestingboard.com/')

# Optional: Wait for a few seconds to see the opened page
import time

time.sleep(5)

# Close the browser
driver.quit()