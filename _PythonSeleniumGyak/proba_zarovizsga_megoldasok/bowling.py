"""importok"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

"""driver létrehozása"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = "http://selenium.oktwebs.training360.com/sl10_proba_zarovizsga/bowling-scorecard.html"

"""függvény mely segítségével adott id szöveget tartalmazó webelementek listáját kapjuk"""
def list_generator(word):
    word_list = driver.find_elements(By.XPATH, f"//td[contains(@id,'{word}')]")
    return word_list

"""függvény mely bármely gombot visszaadja a számát megadva bemeneti paraméterként"""
def find_button(nr):
    return driver.find_element(By.XPATH, f"//button[text()='{nr}']")

# TC1
"""minden, az id-jében frame ill. marker szót tartalmazó webelementek végig iterálás, a lista adott elemének üres szövegére ellenőrzés"""
driver.get(URL)
for frame in list_generator("frame"):
    assert frame.text == ""

for score in list_generator("marker"):
    assert score.text == ""

# TC2
"""11-szer 10-s gomb megnyomása"""
testdata_scores = [10, 20, 40, 60, 80, 100, 120, 140, 160, 200]
driver.get(URL)
for i in range(11):
    find_button(10).click()

"""minden, az id-jében marker szót tartalmazó webelementek végig iterálás, majd a lista adott elemének szövegét - típus konverzióval - külön listába  gyűjtünk"""
scores = []
for score in list_generator("marker"):
    scores.append(int(score.text))

"""a két lista egyezőségét ellenőrizzük"""
assert scores == testdata_scores
time.sleep(1)

# TC3
"""a megadott gombok megnyomásával ellenőrizzük a megjelent üzenet szövegét"""
testdata_message = "Invalid Roll - there are only ten pins!"
driver.get(URL)
find_button(6).click()
find_button(5).click()

assert driver.find_element(By.ID, "comments").text == testdata_message
time.sleep(1)

"""lezárás"""
driver.close()
