# importok
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_age_calculator():
    # driver meghívása
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # oldal megnyitása
    driver.get("http://selenium.oktwebs.training360.com/r2d2_felezovizsga/age_calculator.html")

    # elemek kikeresése
    years_input = driver.find_element(By.ID, "age")
    submit = driver.find_element(By.ID, "submit")
    days = driver.find_element(By.ID, "days")
    hours = driver.find_element(By.ID, "hours")
    minutes = driver.find_element(By.ID, "minutes")
    seconds = driver.find_element(By.ID, "seconds")


    # kitöltő függvény definiálása
    def input_years(years):
        years_input.clear()
        years_input.send_keys(years)
        submit.click()


    # TC_001
    try:
        input_years(39)
        assert minutes.text == "20512440"
        print("TC_001 passed!")
    except:
        print("TC_001 failed!")

    # TC_002
    try:
        input_years("")
        assert seconds.text == "0"
        print("TC_002 passed!")
    except:
        print("TC_002 failed!")

    # TC_003
    try:
        input_years(112)
        assert seconds.text == "3534451200"
        print("TC_003 passed!")
    except:
        print("TC_003 failed!")

    driver.close()
