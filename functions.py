from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time

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

def login(driver):
    #driver.get('https://bookcart.azurewebsites.net/')

    login = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-nav-bar/mat-toolbar/mat-toolbar-row/div[3]/button[2]')))
    login.click()

    username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-login/div/mat-card/mat-card-content/form/mat-form-field[1]/div[1]/div/div[2]/input')))
    username_field.send_keys("aminatest123")

    password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-login/div/mat-card/mat-card-content/form/mat-form-field[2]/div[1]/div/div[2]/input')))
    password_field.send_keys("Amina-test123")

    login_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-login/div/mat-card/mat-card-content/form/mat-card-actions/button')))
    login_btn.click()

    time.sleep(5)

def search(driver):
    #driver.get('https://bookcart.azurewebsites.net/')

    search_bar = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/app-nav-bar/mat-toolbar/mat-toolbar-row/div[2]/app-search/form/input')))
    search_bar.send_keys("Harry Potter and the Deathly Hallows")

    search_result = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div/mat-option')))
    search_result.click()

    time.sleep(5)

def wishlist(driver):
    #driver.get('https://bookcart.azurewebsites.net/')
    
    #login(driver)
    #search(driver)

    book = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-home/div/div[2]/div/div')))
    book.click()

    add_to_wishlist_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-book-details/mat-card/mat-card-content/div[2]/div/app-addtowishlist/button')))
    add_to_wishlist_btn.click()

    open_wishlist = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-nav-bar/mat-toolbar/mat-toolbar-row/div[3]/button[1]')))
    open_wishlist.click()

    time.sleep(5)

def checkout(driver):
    #driver.get('https://bookcart.azurewebsites.net/')

    #login(driver)
    #search(driver)
    #wishlist(driver)

    add_to_cart = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-wishlist/mat-card/mat-card-content/table/tbody/tr/td[4]/app-addtocart/button')))
    add_to_cart.click()

    open_cart = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-nav-bar/mat-toolbar/mat-toolbar-row/div[3]/button[2]')))
    open_cart.click()

    checkout_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-shoppingcart/mat-card/mat-card-content[2]/td[6]/button')))
    checkout_btn.click()

    name = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-checkout/mat-card/mat-card-content/div/div[1]/mat-card-content/form/mat-form-field[1]/div[1]/div/div[2]/input')))
    name.send_keys("My Name")

    address_line_1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-checkout/mat-card/mat-card-content/div/div[1]/mat-card-content/form/mat-form-field[2]/div[1]/div/div[2]/input')))
    address_line_1.send_keys("Address Line 1")

    address_line_2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-checkout/mat-card/mat-card-content/div/div[1]/mat-card-content/form/mat-form-field[3]/div[1]/div/div[2]/input')))
    address_line_2.send_keys("Address Line 2")

    pincode = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-checkout/mat-card/mat-card-content/div/div[1]/mat-card-content/form/mat-form-field[4]/div[1]/div/div[2]/input')))
    pincode.send_keys("123456")

    state = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-checkout/mat-card/mat-card-content/div/div[1]/mat-card-content/form/mat-form-field[5]/div[1]/div/div[2]/input')))
    state.send_keys("State")

    time.sleep(5)

    place_order = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-checkout/mat-card/mat-card-content/div/div[1]/mat-card-content/form/mat-card-actions/button[1]')))
    place_order.click()

    time.sleep(10)

def clear_wishlist(driver):

    open_wishlist = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/app-nav-bar/mat-toolbar/mat-toolbar-row/div[3]/button[1]')))
    open_wishlist.click()

    clear_wishlist = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-wishlist/mat-card/mat-card-header/div[2]/button')))
    clear_wishlist.click()

    time.sleep(5)