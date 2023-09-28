from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Find the most optimal locators for Create Account (Registration) page elements:

# Amazon Logo
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')

# "Create account"
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# Your name input field
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

# Email input field
driver.find_element(By.CSS_SELECTOR, '#ap_email')

# Password input field
driver.find_element(By.CSS_SELECTOR, '#ap_password')

# "Passwords must be at least 6 characters."
driver.find_element(By.XPATH, '//*[text()[contains(.,"Passwords must be at least 6 characters")]]')

# Re-enter password input field
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

# "Create your Amazon account" button
driver.find_element(By.CSS_SELECTOR, '#continue')

# "Conditions of Use" link
driver.find_element(By.CSS_SELECTOR, '#legalTextRow a[href*="condition_of_use"]')

# "Privacy Notice" link
driver.find_element(By.CSS_SELECTOR, '#legalTextRow a[href*="privacy_notice"]')

# "Sign In" link
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis a[href*="signin?"]')
