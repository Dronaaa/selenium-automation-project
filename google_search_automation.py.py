from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys  
import time

#Launching Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open the Google homepage
driver.get("https://www.google.com") 

#  Find the search input box using its 'name' attribute
search_box = driver.find_element(By.NAME, "q") 

#Type a search query into the box
search_box.send_keys("Selenium automation with Python") 

#Press 'Enter' to start the search
search_box.send_keys(Keys.RETURN) 

#Wait for 5 seconds so we can see the results
time.sleep(5)

#Close the browser
driver.quit() 
