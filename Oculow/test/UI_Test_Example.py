from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Oculow import oculow

# Configure lince settings
oculow.set_api_key("iCyZc90jJIVJJEcJUYx/9uP8Eyk3b3SD", "+Le1k0t/htqb1rhE1nkri6C7JOW85yWQ")
oculow.set_app_id("oculow")
oculow.set_baseline_management(oculow.ASSISTED)
oculow.set_comparison_logic(oculow.PIXEL_DIFF)

driver = webdriver.Chrome("C:\\Users\\potos\\Documents\\oculow\\oculow-python-sdk\\chromedriver.exe")

driver.set_window_size(1920, 1080)
# Capture lince website
driver.get("http://www.oculow.com")
assert "Oculow" in driver.title
oculow.capture_screen(driver, "home-page")
driver.implicitly_wait(1000)
driver.get('https://www.oculow.com/plans.html')
oculow.capture_screen(driver, "plans")
driver.get('https://www.oculow.com/contact-us.html')
oculow.capture_screen(driver, "contact-us")
driver.get('https://www.oculow.com/register.html')
oculow.capture_screen(driver, "register")
driver.get('https://www.oculow.com/dashboard/home.html')
oculow.capture_screen(driver, "login")
driver.get('https://www.oculow.com/documentation/index.html')
oculow.capture_screen(driver, "documentation")
driver.get('https://www.oculow.com/blog/index.html')
oculow.capture_screen(driver)
driver.close()
oculow.dispose()
