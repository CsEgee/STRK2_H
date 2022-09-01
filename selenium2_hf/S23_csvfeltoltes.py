# importok
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv

# driver meghívása
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

with open('table_in.csv') as csv_in:
    csvreader = csv.reader(csv_in, delimiter=',')
    next(csvreader)
    for row in csvreader:
        print(row)

# try:
#     # oldal betöltése
#     driver.get("http://selenium.oktwebs.training360.com/another_form.html")
#
#     name = driver.find_element(By.ID, 'fullname')
#     email = driver.find_element(By.ID, 'email')
#     dob = driver.find_element(By.ID, 'dob')
#     phone = driver.find_element(By.ID, 'phone')
# finally:
#     driver.close()
