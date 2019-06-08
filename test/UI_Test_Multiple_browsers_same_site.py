from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import lince

driver = webdriver.Chrome()

# Capture lince website
driver.get("http://www.project-lince.com")
driver.set_window_size(1920, 1080)
assert "Lince" in driver.title
lince.capture_screen(driver, "Lince home - Chrome")

driver.close()

driver = webdriver.Firefox()
driver.get("http://www.project-lince.com")
driver.set_window_size(1920, 1080)
assert "Lince" in driver.title
lince.capture_screen(driver, "Lince home - Firefox")

lince.dispose()
