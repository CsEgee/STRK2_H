#importok
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime, date, time, timezone
import time

# https://www.w3schools.com/python/python_datetime.asp

#driver létrehozása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('http://selenium.oktwebs.training360.com/forms.html')
time.sleep(2)

### HU beállítások esetén

# date: 06/05/2021
var1 = date(2021, 6, 5)
driver.find_element(By.ID, "example-input-date").send_keys(var1.strftime("%Y\t%mm%dd"))

# date/time: 2012.05.05. 05:05:05:555
var2 = datetime(2012, 5, 5, 5, 5, 5, 555000)
driver.find_element(By.ID, "example-input-date-time").send_keys(var2.strftime("%Y.%m.%d. %H:%M:%S:%f"))

# date/time local: 05/12/2000 12:01 PM
var3 = datetime(2000,12,5,12,1,1,1)
driver.find_element(By.ID, "example-input-date-time-local").send_keys(var3.strftime("%Y\t/%m/%d%H:%M"))

# month: December 1995
var4 = date(1995, 12, 1)
driver.find_element(By.ID, "example-input-month").send_keys(var4.strftime("%Y\t%B"))

# Week: Week 52, 2015
var5 = date(2015, 12, 28)
driver.find_element(By.ID, "example-input-week").send_keys(var5.strftime("%W%Y"))

# time: 12:25 AM
var6 = datetime(2012, 5, 5, 12, 25, 5, 555000)
driver.find_element(By.ID, "example-input-time").send_keys(var6.strftime("%H%M"))

driver.find_element(By.XPATH, "/html/body").screenshot('dates.png')

time.sleep(3)

driver.close()

"%I:%M\t%p"