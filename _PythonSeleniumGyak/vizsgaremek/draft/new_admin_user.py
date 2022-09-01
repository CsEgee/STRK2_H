# importok
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from common_functions import login, logout

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# TC06
# előfeltétel megvalósítása (bejelentkezés admin oldalra)
try:
    login(driver, 'admin', 'admin12')
    time.sleep(1)

    # felhasználók oldal megnyitása
    driver.find_element(By.XPATH, '//*[@id="menu"]/li[3]/ul[1]/li[1]/a').click()

    # jelenlegi felhasználók száma
    table_rows = driver.find_elements(By.XPATH, '//*[@id="user"]/tbody/tr')
    table_rows_count = len(table_rows)
    time.sleep(1)

    # új admin felhasználó hozzáadása
    driver.find_element(By.XPATH, '//*[@id="functions"]/a').click()
    driver.find_element(By.XPATH, '//*[@id="generalData"]/fieldset[1]/input[1]').send_keys('admintest')
    driver.find_element(By.XPATH, '//*[@id="generalData"]/fieldset[1]/input[2]').send_keys('admintest12')
    driver.find_element(By.XPATH, '//*[@id="generalData"]/fieldset[1]/input[3]').send_keys('admintest12')
    driver.find_element(By.XPATH, '//*[@id="generalData"]/fieldset[1]/input[4]').send_keys('Teszt')
    driver.find_element(By.XPATH, '//*[@id="generalData"]/fieldset[1]/input[5]').send_keys('Elekina')
    driver.find_element(By.XPATH, '//*[@id="generalData"]/fieldset[1]/input[6]').send_keys('teszt.elekina@mail.com')
    driver.find_element(By.XPATH, '//*[@id="user.role"]/option[4]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="buttons"]/input').click()
    time.sleep(1)

    # firssített felhasználók száma
    table_rows_new = driver.find_elements(By.XPATH, '//*[@id="user"]/tbody/tr')
    table_rows_new_count = len(table_rows_new)

    # hozzáadott elem ellenőrzése
    assert int(table_rows_count) + 1 == int(table_rows_new_count)

    # hozzáadott felhasználó működésének ellenőrzése
    logout(driver)
    time.sleep(1)
    login(driver, 'admintest', 'admintest12')
    time.sleep(1)

    # belépett felhasználó ellenőrzése
    user_logged_in = driver.find_element(By.XPATH, '//*[@id="login"]').text
    assert user_logged_in == 'Logged in: admintest::Administrator | Log out | Help'

    # környezet visszaállítása
    driver.find_element(By.XPATH, '//*[@id="menu"]/li[3]/ul[1]/li[1]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//table[@id="user"]//tbody//tr//td[contains(text(),"admintest")]//following-sibling::td[3]//a[1]').click()
    time.sleep(1)
    alert = driver.switch_to.alert
    time.sleep(1)
    alert.accept()
    logout(driver)
    time.sleep(1)



finally:
    driver.close()
