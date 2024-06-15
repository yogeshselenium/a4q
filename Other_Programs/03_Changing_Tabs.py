from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Specify the path to your WebDriver (e.g., chromedriver)
driver_path = 'C://Program Files//Python310//Scripts//chromedriver.exe'

# Create a Service object with the path to the WebDriver
service = Service(driver_path)

# Create an Options object
options = Options()

# Initialize the WebDriver with the Service and Options objects
driver = webdriver.Chrome(service=service, options=options)

# Open the first link
driver.get('https://magento.softwaretestingboard.com/')

# Open a new tab and switch to it
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])

# Open the second link in the new tab
driver.get('https://www.flipkart.com/')  # Replace with your second URL

# Optional: Wait for a few seconds to see the opened pages
time.sleep(5)

# Store the window handles
window1 = driver.window_handles[0]
window2 = driver.window_handles[1]

# Switch to the first tab
driver.switch_to.window(window1)
print(f"Switched to window: {driver.title}")

# Optional: Wait for a few seconds to see the switched window
time.sleep(5)

# Switch to the second tab
driver.switch_to.window(window2)
print(f"Switched to window: {driver.title}")

# Optional: Wait for a few seconds to see the switched window
time.sleep(5)

# Close the browser
driver.quit()
