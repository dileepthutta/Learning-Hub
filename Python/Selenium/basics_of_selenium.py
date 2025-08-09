from webbrowser import Chrome

from selenium import webdriver

# -------------------JUST TO OPEN THE CHROME AND AUTOMATICALLY STOP THE CHROME AFTER PROGRAM FINISHES---------------------------------
#   Choosing a WebDriver.
driver = webdriver.Chrome()
# To open the specific link.
driver.get("https://www.google.com")

# ---------------------TO OPEN CHROME AND MAKE CHROME TO REMAIN CONSTANT-------------------------------------

# TO KEEP CHROME BROWSER OPEN AFTER THE PROGRAM FINISHES
chrome = webdriver.ChromeOptions()
chrome.add_experimental_option("detach",True)

driver1 = webdriver.Chrome(options=chrome)
driver1.get("https://instagram.com")

#   Quit the entire browser.
driver1.quit()
