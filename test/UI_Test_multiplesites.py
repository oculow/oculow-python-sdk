from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import oculow

driver = webdriver.Chrome("C:\\Users\\potos\\Documents\\oculow\\oculow-python-sdk\\chromedriver.exe")
# Capture apptim website
driver.get("http://www.oculow.com")
assert "Oculow" in driver.title
oculow.capture_screen(driver)

# Capture lince website
# driver.get("http://www.project-lince.com")
# assert "Lince" in driver.title
# lince.capture_screen(driver)

driver.close()
oculow.dispose()
