# importok
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from common_functions import login, logout

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# TC03
# előfeltétel megvalósítása (bejelentkezés admin oldalra)
try:
    login(driver, 'admin', 'admin12')
    time.sleep(1)

    # kilépés
    logout(driver)
    time.sleep(1)

    # kilépés ellenőrzése
    assert driver.current_url == 'http://10.211.55.3:8084/login.htm' or 'http://localhost:8084/login.htm'

finally:
    driver.close()