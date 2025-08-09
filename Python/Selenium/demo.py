from selenium import webdriver
from selenium.webdriver.common.by import By


chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome)
driver.get("https://www.python.org/")

search_bar = driver.find_element(By.NAME,value="q")
button = driver.find_element(By.ID,value="submit")
anchor_tag = driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
xpath = driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')


print(f"To get the Tag Name of the HTML Element :{search_bar.tag_name}")
print(f"To get the placeholder data :{search_bar.get_attribute("placeholder")}")
print(f"To get the information of the button :{button.size}")
print(f"TO print the anchor Tag text {anchor_tag.text}")
print(f"To print the anchor tag using the xpath :{xpath.text}")