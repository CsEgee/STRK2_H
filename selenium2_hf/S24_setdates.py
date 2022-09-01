# importok
import time

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # oldal betöltése
    driver.get("http://selenium.oktwebs.training360.com/forms.html")

    # beviteli mezők kikeresése
    date = driver.find_element(By.ID, 'example-input-date')
    date_time = driver.find_element(By.ID, 'example-input-date-time')
    date_time_local = driver.find_element(By.ID, 'example-input-date-time-local')
    month = driver.find_element(By.ID, 'example-input-month')
    week = driver.find_element(By.ID, 'example-input-week')
    time_input = driver.find_element(By.ID, 'example-input-time')

    # értékek megadása
    date_in = datetime(2021, 6, 5)
    date.send_keys(date_in.strftime('00%Y/%m/%d'))
    date_time_in = datetime(2012, 5, 5, 5, 5, 5, 555)
    date_time.send_keys(date_time_in.strftime('%Y.%m.%d %H:%M:%S:%f'))
    date_time_local_in = datetime(2000, 12, 5, 12, 1)
    date_time_local.send_keys(date_time_local_in.strftime('00%Y/%m/%d %H:%M'))
    month_in = datetime(1995, 12, 1)
    month.send_keys(month_in.strftime('%Y. %B'))
    week_in = datetime(2015, 12, 25)
    week.send_keys(week_in.strftime('%V,%Y'))
    time_input_in = datetime(2022, 5, 30, 12, 25)
    time_input.send_keys(time_input_in.strftime('%H:%M'))
    time.sleep(5)

finally:
    driver.close()
