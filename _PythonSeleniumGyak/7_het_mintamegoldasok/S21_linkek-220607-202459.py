#importok
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

links = []
#driver létrehozása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:

    driver.get("http://selenium.oktwebs.training360.com/")

    # egy listába kigyűjtjük a link elemeket, azaz az anchorokat
    anchors = driver.find_elements(By.XPATH, "//a")

    # a kigyűjtött anchorokhoz tartozó link szöveget for ciklussal kigyűjtjük egy links nevű listába
    for a in anchors:
        links.append(a.get_attribute("href"))


    # a links lista elemeit kiírjuk egy fájlba, itt figyelni kell arra, hogy ha a lista elemek nem string-ek akkor át kell alakítani őket
    # mivel soronként kell kiírni, ezért for ciklussal kell dolgozni, illetve minden elemhez sortörést kell betenni
    with open("links.txt", "w") as file:
        for link in links:
            file.write((link) + "\n")


    print(f"Number of links: {len(links)}")

    time.sleep(1)

finally:
    driver.close()
