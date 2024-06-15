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
driver.get('https://www.geeksforgeeks.org/')
driver.maximize_window()
time.sleep(3)

# Clicking on Sign in button to open the modal
B_Sign_In = driver.find_element(By.XPATH, "//a[contains(text(), 'Sign In')]")
B_Sign_In.click()
time.sleep(5)

# # Demonstrating You directly not select it
# TB_Username = driver.find_element(By.XPATH, "//input[@id='fuser']")
# TB_Username.send_keys("example@technometer.com")
# time.sleep(5)

# Wait for the modal to be present
wait = WebDriverWait(driver, 10)
modal = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='modal-content'])[1]")))

# Locate the username text box within the modal
username_tb = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='luser']")))

# Interact with the username text box
username_tb.send_keys('example@technometer.com')
time.sleep(5)
