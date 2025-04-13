from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Open Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Go to the demo login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Step 3: Find the username field and enter the username
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("student")

# Step 4: Find the password field and enter the password
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("Password123")

# Step 5: Find the login button and click it
login_button = driver.find_element(By.ID, "submit")
login_button.click()

# Step 6: Wait to let the result load
time.sleep(3)

# Step 7: Check if login was successful by finding a specific element
success_message = driver.find_element(By.TAG_NAME, "h1").text

# Step 8: Print result in terminal
if "Logged In Successfully" in success_message:
    print("✅ Login test passed!")
else:
    print("❌ Login test failed.")

# Step 9: Close the browser
driver.quit()
