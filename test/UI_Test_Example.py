from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import lince

driver = webdriver.Chrome()

# Capture lince website
driver.get("http://www.project-lince.com")
assert "Lince" in driver.title
lince.capture_screen(driver)

lince.dispose()
driver.close()