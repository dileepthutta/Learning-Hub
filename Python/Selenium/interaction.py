from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# Open a specific link in the website.
hyper_link_open = driver.find_element(By.LINK_TEXT,value="Site news")
# hyper_link_open.click()

# Find the search input by name
search = driver.find_element(By.NAME,value="search")
search.send_keys("python",Keys.ENTER)

first_name = driver.find_element(By.NAME,value="fName")
first_name.send_keys("Hello")

last_name = driver.find_element(By.NAME,value="lName")
last_name.send_keys("World")

email_field = driver.find_element(By.NAME,value="email")
email_field.send_keys("deepu@gmail.com",Keys.ENTER)

# --------------------------------- OR ------------------------------------------------------
# Find out all the fields
fname = driver.find_element(By.NAME,value="fName")
lname = driver.find_element(By.NAME,value="lName")
email = driver.find_element(By.NAME,value="email")

# Fill out the form
fname.send_keys("Allu")
lname.send_keys("Arjun")
email.send_keys("iconstar@gmail.com")

# Sign up button Click.
submit = driver.find_element(By.CSS_SELECTOR,value="form button")
submit.click()