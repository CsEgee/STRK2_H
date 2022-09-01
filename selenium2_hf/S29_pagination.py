import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # oldal betöltése
    driver.get("http://selenium.oktwebs.training360.com/pagination.html")

    next_button = driver.find_element(By.ID, 'next')
    while True:
        if next_button.is_enabled():
            time.sleep(1)
            next_button.click()
        else:
            break

    time.sleep(2)
finally:
    driver.close()
