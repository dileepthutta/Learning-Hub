from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Open a specific link in the website.
hyper_link_open = driver.find_element(By.LINK_TEXT,value="Site news")
hyper_link_open.click()