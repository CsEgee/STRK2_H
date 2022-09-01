# importok
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from common_functions import login, logout

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# TC09
# előfeltétel megvalósítása (bejelentkezés admin oldalra)
try:
    login(driver, 'admin', 'admin12')
    time.sleep(1)

    # programok oldal megnyitása
    driver.find_element(By.XPATH, '//*[@id="menu"]/li[3]/ul[1]/li[2]/a').click()
    time.sleep(1)

    # Medicine (MD) nevű elem szerkesztőablakának megnyitása
    driver.find_element(By.XPATH, '//table[@id="program"]//tbody//tr//td[contains(text(),"GENMED")]//following-sibling::td[3]//a[2]').click()

    # Medicine (MD) nevének átírása General Medicine (MD)-re
    genmed_name = driver.find_element(By.ID, 'program.programName')
    genmed_name.clear()
    genmed_name.send_keys('General Medicine (MD)')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="buttons"]/input').click()
    time.sleep(1)

    # változtatott programnév ellenörzése
    genmed_new_name = driver.find_element(By.XPATH, '//table[@id="program"]//tbody//tr//td[contains(text(),"GENMED")]//following-sibling::td[1]').text
    assert genmed_new_name == 'General Medicine (MD)'

    # környezet visszaállítása
    driver.find_element(By.XPATH,'//table[@id="program"]//tbody//tr//td[contains(text(),"GENMED")]//following-sibling::td[3]//a[2]').click()
    genmed_name = driver.find_element(By.ID, 'program.programName')
    genmed_name.clear()
    genmed_name.send_keys('Medicine (MD)')
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="buttons"]/input').click()
    time.sleep(1)

    # kilépés
    logout(driver)
    time.sleep(1)

finally:
    driver.close()
