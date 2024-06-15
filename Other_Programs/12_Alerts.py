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
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()
time.sleep(3)

# Clicking on Try it button to open the alert
B_JS_Alert = driver.find_element(By.XPATH, "//button[contains(text(), 'Click for JS Alert')]")
B_JS_Alert.click()
time.sleep(5)


# Alert E.g.
Alert_window = driver.switch_to.alert

# Text
text_on_alert = Alert_window.text
print(text_on_alert)

# accept
Alert_window.accept()
time.sleep(3)

# Dismiss
B_JS_Alert = driver.find_element(By.XPATH, "//button[contains(text(), 'Click for JS Confirm')]")
B_JS_Alert.click()
time.sleep(3)

Alert_window.dismiss()
time.sleep(3)
