"""importok"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

"""driver létrehozása"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = "http://selenium.oktwebs.training360.com/sl10_proba_zarovizsga/periodic_table.html"

driver.get(URL)

"""a periódusus rendszer elemeinek, mint webelementek kigyűjtése listába"""
periodic_table_elements = driver.find_elements(By.XPATH, '//li[@class!="empty"]')

"""fájl beolvasása, beolvasása soronként, enumerate függvény segítségével az egyes lista elemhez tartozó index és tartalom felhasználása, az egyes beolvasott sorok tartalmának szétbontása a , mentén, az elemek sorszámára és név szövegére ellenőrzés """
with open("data.txt", "r") as test_data:
    for index, row in enumerate(test_data.readlines()):
        row = row.split(", ")
        element_number = periodic_table_elements[index].get_attribute("data-pos")
        assert element_number == row[0]
        element_name = periodic_table_elements[index].find_element(By.TAG_NAME, "span").text
        assert element_name == row[1].replace("\n", "")

"""lezárás"""
driver.close()