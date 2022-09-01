#importok
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

#driver létrehozása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:

    base_url = "http://selenium.oktwebs.training360.com/general.html"
    start_page = "http://selenium.oktwebs.training360.com/"
    driver.get(base_url)

#elemek kikeresése
    anchors = driver.find_elements(By.XPATH, '//header//small//a')

#feladat első rész
    print("-"*20 + "1.task" + "-"*20)

#műveletek az elemekkel
    for a in anchors:
        a.click()
        print(driver.current_url)
        print(a.get_attribute("href"))
        assert driver.current_url == a.get_attribute("href")
        if driver.current_url == a.get_attribute("href"):
            print("anchor was clicked")
            driver.back()
            print(driver.current_url)
        if driver.current_url == base_url:
            print("back navigation was successful")

#feladat második rész
    print("-" * 20 + "2.task" + "-" * 20)

#műveletek az elemekkel
    for a in anchors:
        a.click()
        if "phrasing" in driver.current_url:            #ugyanez a sor alternatív módon => if driver.current_url.endswith("phrasing"):
            if driver.current_url == a.get_attribute("href"):
                print(driver.current_url)
                print(a.get_attribute("href"))
                print("anchor was clicked")
                driver.get(start_page)
                print(driver.current_url)
                print("open of start page was successful")
                assert driver.current_url == start_page
                break
        else:
            print(driver.current_url)
            print(a.get_attribute("href"))
        if driver.current_url == a.get_attribute("href"):
            print("anchor was clicked")
            driver.back()
            print(driver.current_url)
        if driver.current_url == base_url:
            print("back navigation was successful")

#kivételkezelés
except NoSuchElementException as e:
    print('Element not found: ', e)

#lezárás
finally:
    driver.close()
