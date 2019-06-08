from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import lince

driver = webdriver.Chrome()
# Capture apptim website
driver.get("http://www.apptim.com")
assert "Apptim" in driver.title
lince.capture_screen(driver)

# Capture lince website
driver.get("http://www.project-lince.com")
assert "Lince" in driver.title
lince.capture_screen(driver)

lince.dispose()
driver.close()