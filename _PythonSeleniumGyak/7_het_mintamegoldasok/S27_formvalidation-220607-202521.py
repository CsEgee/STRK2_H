# importok
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import string

# driver létrehozása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = "http://selenium.oktwebs.training360.com/simplevalidation.html"

#Helytelen kitöltés függvénye
def fill_wrong(field_id, t1):
    driver.get(URL)
    field = driver.find_element(By.ID, field_id)
    field.send_keys(t1)
    id_attr = field.get_attribute("data-jsv-message-target")
    time.sleep(2.5)
    return driver.find_element(By.ID, id_attr).text

#Helyes kitöltés függvénye
def fill_right(field_id, t1):
    driver.get(URL)
    field = driver.find_element(By.ID, field_id)
    field.send_keys(t1)
    id_attr = field.get_attribute("data-jsv-message-target")
    time.sleep(2.5)
    return driver.find_element(By.ID, id_attr)


try:
    # TC1 : E-mail mező üres
    assert fill_wrong("test-email", Keys.TAB) == "Please enter an e-mail"

    # TC2 : E-mail mező @ nélkül
    assert fill_wrong("test-email", "wrongvemail") == "Please check your E-Mail format"

    # TC3 : Nem létező e-mailcím
    assert fill_wrong("test-email", f"{random.choice(string.ascii_lowercase)}{random.randint(10, 1000)}@mail.xyz") == "Login does not exist"

    # TC4 : Létező e-mailcím
    assert not fill_right("test-email", "yardy@yarr.com").is_displayed()

    # TC5 : Random mező üres
    assert not fill_right("test-random-field", "\t").is_displayed()

    # TC6 : Random mező helyes tartalommal kitöltve
    assert not fill_right("test-random-field", "twelve").is_displayed()

    # TC7 : Random mező helytelen tartalommal kitöltve
    assert fill_wrong("test-random-field", "www") == 'Should contain "twelve"'

    # TC8 : Kártyaszám mező üres
    assert fill_wrong("test-card-number", "\t") == "Please enter a credit card number (no spaces)"

    # TC9 : Kártyaszám mező helytelen tartalommal kitöltve
    assert fill_wrong("test-card-number", random.randint(4, 6)) == "Please check your credit card nubmer"

    # TC10 : Kártyaszám mező helyes tartalommal kitöltve
    assert not fill_right("test-card-number", 4111111111111111).is_displayed()


finally:
    driver.close()
