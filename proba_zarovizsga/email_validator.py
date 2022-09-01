# importok
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def fill_email(email):
    # elemek kikeresése
    email_input = driver.find_element(By.ID, 'email')
    submit_btn = driver.find_element(By.ID, 'submit')
    # mező törlése, kitöltés és gomb kattintás
    email_input.clear()
    email_input.send_keys(email)
    time.sleep(1)
    submit_btn.click()
    time.sleep(1)

try:

    # oldal megnyitása
    driver.get('http://selenium.oktwebs.training360.com/sl10_proba_zarovizsga/email_validator.html')

    # TC1 Helyes kitöltés esete:
    fill_email('teszt@elek.hu')
    assert driver.find_element(By.XPATH, '/html/body/div/div/form').get_attribute('class') == ''
    print('TC1 pass')

    # TC2 Helytelen kitöltés esete:
    fill_email('teszt@')
    assert driver.find_element(By.XPATH, '/html/body/div/div/form/div[@class="validation-error"]').text == 'Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.'
    print('TC2 pass')

    # TC3 Üres kitöltés esete:
    fill_email('')
    assert driver.find_element(By.XPATH, '/html/body/div/div/form/div[@class="validation-error"]').text == 'Kérjük, töltse ki ezt a mezőt.'
    print('TC3 pass')

finally:
    driver.close()