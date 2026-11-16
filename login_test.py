# Code to implement above

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open Chrome
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

try:
    # Open practice login page
    driver.get("https://the-internet.herokuapp.com/login")

    # Test 1: Valid login
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    if "You logged into a secure area!" in message.text:
        print("Test 1: PASS - Valid login")
    else:
        print("Test 1: FAIL - Valid login")

    # Test 2: Invalid password
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("wrong123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    )

    if "Your password is invalid!" in message.text:
        print("Test 2: PASS - Invalid password")
    else:
        print("Test 2: FAIL - Invalid password")

finally:
    # Close browser
    driver.quit()
