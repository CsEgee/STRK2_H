import time
import traceback

from selenium import webdriver

# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# from selenium.common.exceptions import NoSuchElementException

# driver létrehozasa többféle módon is lehetséges
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome()
url = "http://selenium.oktwebs.training360.com/editable-table.html"

try:
    driver.get(url)
    time.sleep(1)

    # 1st row, 1st input - where everything starts
    element = driver.find_element(By.XPATH, "//table/tbody/tr[1]/td[1]/input")
    print(element.get_attribute("value"))  # to visualize
    print("=" * 100)

    # number of rows, number of columns - find everything
    rows = len(driver.find_elements(By.XPATH, "//table/tbody/tr"))
    columns = 4
    for i in range(rows):
        for j in range(columns):
            element = driver.find_element(By.XPATH, f"//table/tbody/tr[{i + 1}]/td[{j + 1}]/input")
            print(element.get_attribute("value"))  # to visualize
    print("=" * 100)

    # List of lists - collect everything in lists
    sorok = []  # as first dimension
    for i in range(rows):
        oszlopok = []  # as second dimension
        for j in range(columns):
            element = driver.find_element(By.XPATH, f"//table/tbody/tr[{i + 1}]/td[{j + 1}]/input")
            oszlopok.append(element.get_attribute("value"))
            # print(element.get_attribute("value"))
        sorok.append(oszlopok)

    print(sorok)  # to visualize
    print("=" * 100)

    # column - if only one certain column is needed
    elements = driver.find_elements(By.XPATH, "//table/tbody/tr/td/input[@name='name']")
    names = []
    for e in elements:
        names.append(e.get_attribute("value"))
    print(names)  # to visualize

except Exception as e:  # az assert által dobott exception-t is elapja!
    print("Element not found or assert False!")
    traceback.print_exception(e)
finally:
    driver.close()
