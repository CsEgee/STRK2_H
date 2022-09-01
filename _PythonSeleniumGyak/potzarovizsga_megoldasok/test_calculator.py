"""importok"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

"""driver létrehozása"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = "http://selenium.oktwebs.training360.com/7904_potzarovizsga/calculator.html"

def digit_clicking(digit):
    driver.find_element(By.XPATH, f"//*[@class='digit-keys']//button[text()='{digit}']").click()

def operator_clicking(op):
    driver.find_element(By.XPATH, f"//*[@class='operator-keys']//button[text()='{op}']").click()

def function_clicking(func):
    driver.find_element(By.XPATH, f"//*[@class='function-keys']//button[text()='{func}']").click()

ware_1_nett = "1000"
ware_2_nett = "3000"
vat = "27"

# TC_001
def test_calculator_tc1():
    driver.get(URL)
    for d in ware_1_nett:
        digit_clicking(d)
    operator_clicking("+")
    for d in ware_2_nett:
        digit_clicking(d)
    operator_clicking("=")

    nett_sum = driver.find_element(By.CLASS_NAME, "auto-scaling-text").text
    # assert nett_sum == "4 000"

    function_clicking("%")
    operator_clicking("×")
    for v in vat:
        digit_clicking(v)
    operator_clicking("=")

    vat_sum = driver.find_element(By.CLASS_NAME, "auto-scaling-text").text
    assert vat_sum == "1 080"

    for d in (nett_sum.replace(" ", "")):
        digit_clicking(d)
    operator_clicking("+")
    for d in (vat_sum.replace(" ", "")):
        digit_clicking(d)
    operator_clicking("=")

    gross_sum = driver.find_element(By.CLASS_NAME, "auto-scaling-text").text
    assert gross_sum == "5 080"


    """lezárás"""
    driver.close()