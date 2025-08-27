import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome)
driver.get("https://www.tutorialspoint.com/index.htm")

# Wait for the page to fully load
time.sleep(3)

# Now find the search box and send text
search_box = driver.find_element(By.XPATH, '//*[@id="search-strings"]')
search_box.send_keys("Hello")
