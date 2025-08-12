from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=chrome)
driver.get("https://www.python.org/")

get_time = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
get_name = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")

#To create a dictionary which contains time and name.
events = {}

for i in range(0,len(get_time)):
    events[i] = {
        "time" :get_time[i].text,
        "name" :get_name[i].text
    }
print(events)