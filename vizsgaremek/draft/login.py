# importok
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from common_functions import login, logout

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # login oldal betöltése és bejelentkezés admin / admin12 kredenciálissal
    login(driver, 'admin', 'admin12')
    time.sleep(1)

    # várt URL ellenőrzése
    assert driver.current_url == 'http://10.211.55.3:8084/eduardStartPage.htm' or 'http://localhost:8084/eduardStartPage.htm'

    # beléptetett felhasználó ellenőrzése
    user_logged_in = driver.find_element(By.XPATH, '//*[@id="login"]').text
    assert user_logged_in == 'Logged in: admin::Administrator | Log out | Help'

    # kilépés
    logout(driver)
    time.sleep(1)

    # TC02 sikertelen belépés admin / admin kredenciálisokkal
    login(driver, 'admin', 'admin')
    time.sleep(1)
    assert driver.find_element(By.XPATH, '//*[@id="loginData"]/fieldset[1]/div').text == 'Login failed!'

finally:
    driver.close()
