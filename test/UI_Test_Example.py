from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import oculow

# Configure lince settings
oculow.set_api_key("9HanEbAexPF2cPAJzlFNXBIGNzqhK2pU", "uTLZZLR/HnUOCu5U7vNI6WrsYTBGTBxM")
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
