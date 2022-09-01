"""importok"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

"""driver létrehozása"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
URL = "http://selenium.oktwebs.training360.com/7709_zarovizsga/matek_app.html"


def find_text(id):
    return driver.find_element(By.ID, id).text

def find_click(id):
    driver.find_element(By.ID, id).click()

# TC_001
driver.get(URL)
time.sleep(1)
assert driver.find_element(By.ID, "submit").is_enabled()
assert find_text("result") == ""

# TC_002
driver.get(URL)
time.sleep(1)
find_click("submit")
check_point = find_text("result")
for i in range(3):
    find_click("submit")
    assert find_text("result") == check_point

# TC_003
driver.get(URL)
time.sleep(1)

def calculation_process():
    # Kikeressük a számokat és a műveleti jeleket
    first_number = int(find_text("num1"))
    operator_character1 = find_text("op1")
    second_number = int(find_text("num2"))
    operator_character2 = find_text("op2")
    third_number = int(find_text("num3"))
    find_click("submit")
    time.sleep(1)

    # Az alkalmazás által számolt eredményt összehasonlítjuk a saját számításunkkal
    calculated_result_by_app = int(find_text("result"))

    # A saját számításunkhoz az app számait és műveleti jeleit használjuk, azért alkalmazunk elágazást, mert a műveleti jelet ilyen formában lehet csak megfogni
    if operator_character1 == "+" and operator_character2 == "+":
        assert calculated_result_by_app == (first_number + second_number + third_number)
        print(first_number + second_number + third_number)
    elif operator_character1 == "-" and operator_character2 == "-":
        assert calculated_result_by_app == (first_number - second_number - third_number)
        print(first_number - second_number - third_number)
    elif operator_character1 == "*" and operator_character2 == "*":
        assert calculated_result_by_app == (first_number * second_number * third_number)
        print(first_number * second_number * third_number)
    elif operator_character1 == "+" and operator_character2 == "-":
        assert calculated_result_by_app == (first_number + second_number - third_number)
        print(first_number + second_number - third_number)
    elif operator_character1 == "-" and operator_character2 == "+":
        assert calculated_result_by_app == (first_number - second_number + third_number)
        print(first_number - second_number + third_number)
    elif operator_character1 == "+" and operator_character2 == "*":
        assert calculated_result_by_app == (first_number + second_number * third_number)
        print(first_number + second_number * third_number)
    elif operator_character1 == "*" and operator_character2 == "+":
        assert calculated_result_by_app == (first_number * second_number + third_number)
        print(first_number * second_number + third_number)
    elif operator_character1 == "-" and operator_character2 == "*":
        assert calculated_result_by_app == (first_number - second_number * third_number)
        print(first_number - second_number * third_number)
    elif operator_character1 == "*" and operator_character2 == "-":
        assert calculated_result_by_app == (first_number * second_number - third_number)
        print(first_number * second_number - third_number)
    print(calculated_result_by_app)

# Maga a teszt, amikor 10-szer egymás után ismételjük a fentiekben leírt számítási folyamatot
for i in range(10):
    driver.refresh()
    print(i+1, "round")
    calculation_process()
    time.sleep(0.5)

time.sleep(1)

"""lezárás"""
driver.close()