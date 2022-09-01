#importok
import csv
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#driver létrehozása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('http://selenium.oktwebs.training360.com/another_form.html')

#webelement megadása
def find_and_clear(id):
    element = driver.find_element(By.ID, id)
    element.clear()
    return element

input_csv_content = []

with open('table_in.csv', encoding='utf-8') as csvfile:
    input_csv = csv.reader(csvfile, delimiter=',')              # megadjuk, hogy mit olvasson a csv olvasó, valamint azt, hogy milyen elválasztót használtunk( ez lehet , és ; stb)
    next(input_csv)                                             # erre azért van szükség, mert az első sor csak a fejléc, konkrét értékeket nem tartalmaz
    for row in input_csv:                                       # for ciklus segítségével töltjük be az adatokat
        input_csv_content.append(row)
        # print(row)
        find_and_clear("fullname").send_keys(row[0])

        find_and_clear("email").send_keys(row[1])

        find_and_clear("dob").send_keys(row[2])

        find_and_clear("phone").send_keys(row[3])

        submit = driver.find_element(By.ID, "submit")
        submit.click()


driver.find_element(By.XPATH, "/html/body/main/div/button").click()
time.sleep(1)


result_csv_content = []

with open("C:\\Users\\szita\\Downloads\\table.csv", encoding='utf-8') as result_file:
    result_csv = csv.reader(result_file, delimiter=',')                 # megadjuk, hogy mit és honnan olvasson a csv olvasó, valamint azt, hogy milyen elválasztót használtunk( ez lehet , és ; stb)
    print(result_csv)
    next(result_csv)                                                    # erre azért van szükség, mert az első sor csak a fejléc, konkrét értékeket nem tartalmaz
    for row in result_csv:
        result_csv_content.append(row)


print(type(input_csv_content))
print(input_csv_content)
print(type(result_csv_content))
print(result_csv_content)


assert input_csv_content == result_csv_content                           # összehasonlítjuk a betöltött adatokat és a letöltött adatokat tartalmazó listát


os.remove("C:\\Users\\szita\\Downloads\\table.csv")                      # töröljük a legenerált csv-t, hogy újra ismételhető legyen a teszt



time.sleep(2)

driver.close()

