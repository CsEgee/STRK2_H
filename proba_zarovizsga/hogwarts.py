# importok
import time as time_
from datetime import datetime, date, time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def fill_ticket(passenger, ddate, dtime):
    # elemek kikereése
    passenger_in = driver.find_element(By.ID, 'passenger')
    ddate_in = driver.find_element(By.ID, 'departure-date')
    dtime_in = driver.find_element(By.ID, 'departure-time')
    issue_btn = driver.find_element(By.ID, 'issue-ticket')
    # mezők törlése, kitöltése és kattintás
    passenger_in.clear()
    passenger_in.send_keys(passenger)
    ddate_in.clear()
    ddate_in.send_keys(ddate.strftime("%Y\t%mm%dd"))
    dtime_in.send_keys(dtime.strftime("%H%M"))
    time_.sleep(1)
    issue_btn.click()
    time_.sleep(1)


def assert_ticket(passenger, ddate, dtime):
    ticket_name = driver.find_element(By.ID, 'passenger-name').text
    ticket_date = driver.find_element(By.ID, 'departure-date-text').text
    ticket_time = driver.find_element(By.ID, 'departure-time-text').text
    side_date = driver.find_element(By.ID, 'side-detparture-date').text
    side_time = driver.find_element(By.ID, 'side-departure-time').text
    assert ticket_name == passenger.upper()
    assert ticket_date == str(ddate.strftime("%Y-%m-%d"))
    assert ticket_time == str(dtime.strftime("%I:%M%p"))
    assert side_date == str(ddate.strftime("%Y-%m-%d"))
    assert side_time == str(dtime.strftime("%I:%M%p"))

try:
    # oldal megnyitása
    driver.get('http://selenium.oktwebs.training360.com/sl10_proba_zarovizsga/hogwarts.html')

    # TC1 Teljes kitöltés esete:
    fill_name = 'Harry Potter'
    fill_date = date(2022, 10, 1)
    fill_time = time(10, 00)
    fill_ticket(fill_name, fill_date, fill_time)
    assert_ticket(fill_name, fill_date, fill_time)
    print('TC1 pass')

    # TC2 Részleges kitöltés esete:
    fill_name = ''
    fill_date = date(2022, 10, 1)
    fill_time = time(10, 00)
    fill_ticket(fill_name, fill_date, fill_time)
    assert_ticket(fill_name, fill_date, fill_time)
    print('TC2 pass')

    # TC3 Hiányos kitöltés esete: // sajnos ezzel elakadok ott, hogy a készített kitöltő függvénynek nem tudom átadni csak az évet //
    # fill_name = 'Harry Potter'
    # fill_date = date(2022, 10, 1).year
    # fill_time = time(10, 00)
    # fill_ticket(fill_name, fill_date, fill_time)
    # # assert_ticket(fill_name, fill_date, fill_time)
    # print('TC3 pass')

finally:
    driver.close()