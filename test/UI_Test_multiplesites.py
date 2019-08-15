from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import oculow

driver = webdriver.Chrome("./chromedriver")
# Capture apptim website
driver.get("http://www.oculow.com")
assert "Google" in driver.title
oculow.capture_screen(driver)

# Capture lince website
# driver.get("http://www.project-lince.com")
# assert "Lince" in driver.title
# lince.capture_screen(driver)

driver.close()
oculow.dispose()
