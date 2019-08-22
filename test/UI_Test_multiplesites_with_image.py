from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import oculow

driver = webdriver.Chrome()
# Capture apptim website
driver.get("http://www.google.com")
assert "Google" in driver.title
oculow.capture_screen(driver)

# Capture lince website
driver.get("http://www.project-lince.com")
assert "Lince" in driver.title
oculow.capture_screen(driver)

oculow.upload_image("C:\\Users\\Potosin\\Desktop\\test1.PNG")

driver.close()
oculow.dispose()
