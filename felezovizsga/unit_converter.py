# importok
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# oldal megnyitása
driver.get("http://selenium.oktwebs.training360.com/r2d2_felezovizsga/unit_converter.html")

# elemek kikeresése
number_in = driver.find_element(By.ID, "number")
unit_in = driver.find_element(By.ID, "unit")
result = driver.find_element(By.CLASS_NAME, "conversion")


# kitöltő függvény definiálása
def unit_converter(number, unit):
    number_in.clear()
    unit_in.clear()
    number_in.send_keys(number)
    unit_in.send_keys(unit)


# number_in.clear()
# unit_in.clear()
# number_in.send_keys("112")
# unit_in.send_keys("meter")
# print(str(result.text))

# TC_001
try:
    unit_converter("112", "meter")
    assert result.text == "367.45 FOOT"
    print("TC_001 passed!")
except:
    print("TC_001 failed!")

# TC_002
try:
    unit_converter("8", "oz")
    assert result.text == "236.56 MILLILITER"
    print("TC_002 passed!")
except:
    print("TC_002 failed!")

# TC_003
try:
    unit_converter("1", "gallon")
    assert result.text == "3.79 LITER"
    print("TC_002 passed!")
except:
    print("TC_002 failed!")

driver.close()
