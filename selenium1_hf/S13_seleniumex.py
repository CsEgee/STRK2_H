from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def findelemetbyid(idtag):
    try:
        element = driver.find_element(By.ID, idtag)
        return element
    except:
        element = 0
        return element


url_in = input("Add meg a weboldal címét http://")
id_in = input("Add meg a keresendő azonosítót (ID): ")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://" + url_in)

if findelemetbyid(id_in) == 0:
    print("A megadott '" + id_in + "' ID ezen az oldalon NEM található!")
else:
    print("A megadott '" + id_in + "' ID az oldalon megtalálható!")

driver.close()
