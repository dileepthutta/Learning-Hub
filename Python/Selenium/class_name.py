from selenium import webdriver
from selenium.webdriver.common.by import By

# TO KEEP CHROME BROWSER OPEN AFTER THE PROGRAM FINISHES
chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach",True)

driver1 = webdriver.Chrome(options=chrome)
driver1.get("https://a.co/d/a8Cms12")

# To print the data inside the html tags using Class Selectors
dollar_price = driver1.find_element(By.CLASS_NAME,value="a-price-whole")
dollar_cents = driver1.find_element(By.CLASS_NAME,value="a-price-fraction")

print(f"Price of a product is {dollar_price.text}.{dollar_cents.text}")