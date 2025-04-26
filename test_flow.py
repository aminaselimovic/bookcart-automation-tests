from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time
from functions import *

# Path to the chromedriver executable
driver_path = '/Users/amina/Desktop/Selenium/chromedriver-mac-arm64/chromedriver'

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
chrome_options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
# chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)

# Set the path to chromedriver as an environment variable
os.environ['webdriver.chrome.driver'] = driver_path

# Create an instance of the Chrome WebDriver with the specified options
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://bookcart.azurewebsites.net/')

login(driver)
search(driver)
wishlist(driver)
checkout(driver)
clear_wishlist(driver)