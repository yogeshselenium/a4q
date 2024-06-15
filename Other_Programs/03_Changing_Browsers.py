from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Specify the path to your WebDriver
driver_path = "C://Program Files//Python310//Scripts//chromedriver.exe"

# Create a Service object with the path to the WebDriver
service = Service(driver_path)

# Create an Options object
options = Options()

# Initialize the WebDriver_1 (Chrome in this example)
driver_1 = webdriver.Chrome(service=service, options=options)

# Open the website_1
driver_1.get('https://magento.softwaretestingboard.com/')
driver_1.maximize_window()

# Initialize the WebDriver_2 (Chrome in this example)
driver_2 = webdriver.Chrome(service=service, options=options)

# Open the website_2
driver_2.get('https://www.flipkart.com/')
driver_2.maximize_window()

time.sleep(5)

# Store the window handles
window1 = driver_1.current_window_handle
window2 = driver_2.current_window_handle

# Switch to the first window
driver_1.switch_to.window(window1)
print(f"Switched to window: {driver_1.title}")

# Optional: Wait for a few seconds to see the switched window
time.sleep(5)

# Switch to the second window
driver_2.switch_to.window(window2)
print(f"Switched to window: {driver_2.title}")

# Optional: Wait for a few seconds to see the switched window
time.sleep(5)

# Close the browsers
driver_1.quit()
driver_2.quit()
