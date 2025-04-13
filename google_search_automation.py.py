# Importing necessary modules from Selenium
from selenium import webdriver  # To control the browser
from selenium.webdriver.common.by import By  # To locate elements on the page
from selenium.webdriver.common.keys import Keys  # To simulate keyboard actions
import time  # To add delays

# Step 1: Launch Chrome browser
driver = webdriver.Chrome()  # This opens a new Chrome browser window
driver.maximize_window()  # Maximizes the browser window for better visibility

# Step 2: Open the Google homepage
driver.get("https://www.google.com")  # Navigates to Google's homepage

# Step 3: Find the search input box using its 'name' attribute
search_box = driver.find_element(By.NAME, "q")  # Locates the search box element

# Step 4: Type a search query into the box
search_box.send_keys("Selenium automation with Python")  # Types the query into the box

# Step 5: Press 'Enter' to start the search
search_box.send_keys(Keys.RETURN)  # Simulates pressing the Enter key

# Step 6: Wait for 5 seconds so we can see the results
time.sleep(5)  # Waits for 5 seconds (adjustable if needed)

# Step 7: Close the browser
driver.quit()  # Closes the browser window and ends the session
