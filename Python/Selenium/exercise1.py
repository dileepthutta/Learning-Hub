from selenium import webdriver
from selenium.webdriver.common.by import By


chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=chrome)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

data =driver.find_element(By.XPATH,value='//*[@id="articlecount"]/ul/li[2]/a[1]')
print(data.text)