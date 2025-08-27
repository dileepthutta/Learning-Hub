from selenium import webdriver
import time

#------------------------------------------To open chrome and maximize the screen and wait's for 5 seconds.------------------------------------------
# driver = webdriver.Chrome()
#
# driver.get(
#     url="https://google.com"
# )
# driver.maximize_window()
# time.sleep(5)
# driver.quit()

# ------------------------------------------Basic Navigation between the sites.------------------------------------------
# Process
# 1)open's google wait's for 5 seconds
# 2)open's Youtube wait's for 5 seconds
# 3)Again open's google wait's for 5 seconds
# 4)Again open's Youtube wait's for 5 seconds
# 5) Exit
driver1 = webdriver.Chrome()
driver1.maximize_window()

driver1.get("https://www.google.com")

time.sleep(5)

driver1.get("https://www.youtube.com")
driver1.back()
time.sleep(5)
driver1.forward()
driver1.quit()
