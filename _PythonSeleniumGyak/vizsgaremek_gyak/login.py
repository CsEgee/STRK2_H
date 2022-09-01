# importok
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # login oldal betöltése
    try:
        driver.get('http://10.211.55.3:8084/login.htm')
    except:
        driver.get('http://localhost:8084/login.htm')

    # elemek kikeresése és belépés admin / admin12 kredenciálisokkal
    driver.find_element(By.ID, 'username').send_keys('admin')
    driver.find_element(By.NAME, 'j_password').send_keys('admin12')
    driver.find_element(By.CLASS_NAME, 'button').click()
    time.sleep(2)

    # várt URL ellenőrzése
    assert driver.current_url == 'http://10.211.55.3:8084/eduardStartPage.htm' or 'http://localhost:8084/eduardStartPage.htm'

    # beléptetett felhasználó ellenőrzése
    loggedin_user = driver.find_element(By.XPATH, '//*[@id="login"]').text
    print(loggedin_user)
    assert loggedin_user == 'Logged in: admin::Administrator | '

    # kilépés
    driver.find_element(By.XPATH, '//*[@id="login"]/a[1]').click()
    time.sleep(2)

    # kilépés ellenőrzése
    # assert driver.current_url == 'http://10.211.55.3:8084/login.htm' or 'http://localhost:8084/login.htm'

finally:
    driver.close()
