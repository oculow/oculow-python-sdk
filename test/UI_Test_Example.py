from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import oculow

# Configure lince settings
oculow.set_api_key("b5bd77ef-4da5-498e-92df-7d8cd2c9b356")
oculow.set_app_id("oculow")
oculow.set_baseline_management(oculow.ASSISTED)
oculow.set_comparison_logic(oculow.PIXEL_DIFF)

driver = webdriver.Chrome()

# Capture lince website
driver.get("http://www.oculow.com")
assert "Oculow" in driver.title
oculow.capture_screen(driver)

driver.close()
oculow.dispose()
