#importok
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import csv
import pprint

#driver létrehozása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://selenium.oktwebs.training360.com/pagination.html")

extracted_data = []


try:
    while True:
        time.sleep(2)
        #minden A betűvel kezdődő keresztnév sorát listába gyűjtünk
        firstname_with_a_rows = driver.find_elements(By.XPATH,
            "//table[@id='contacts-table']/tbody/tr/td[2][starts-with(text(),'A')]/parent::tr")         # xpath -> lásd cheatsheet

        #a listába gyűjtött sorok celláiból kinyerjük az adatokat
        for row in firstname_with_a_rows:
            data_row = {}
            cells = row.find_elements(By.TAG_NAME, "td")
            data_row["id"] = cells[0].text
            data_row["first_name"] = cells[1].text
            data_row["second_name"] = cells[2].text
            data_row["surname"] = cells[3].text
            data_row["second_surname"] = cells[4].text
            data_row["birth_date"] = cells[5].text
            extracted_data.append(data_row)

        next_button = driver.find_element(By.ID, "next")
        if not next_button.is_enabled():
            break                                                                   # ha már nem elérhető a next button, akkor kitörünk a ciklusból
        else:
            next_button.click()

    # pprint.pprint(extracted_data)                                                   # Pretty-print, mint szebb formátumú megjelenítés
    # print(len(extracted_data))


    with open('result_data.csv', 'w') as resultdata:
        for row in extracted_data:
            resultdata.writelines(f'{row}\n')


    time.sleep(2)
finally:
    driver.close()




