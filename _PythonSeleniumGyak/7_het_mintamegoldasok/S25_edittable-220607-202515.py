# importok
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random
import string

# driver létrehozása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = 'http://selenium.oktwebs.training360.com/editable-table.html'

# TC1 : Két új sor kitöltése
driver.get(URL)

list = ['ham', '10.99', '5', 'Food']
# list = ["".join([random.choice(string.ascii_lowercase) for _ in range(8)]), random.randint(10, 1000),
#         random.randint(10, 100), "".join([random.choice(string.ascii_lowercase) for _ in range(8)])]

need_to_fill_row = 2

start_number_of_rows = len(driver.find_elements(By.XPATH, "//tr[@class='eachRow']"))

add_button = driver.find_element(By.XPATH, '//button[text()="Add"]')


# egy sor feltöltése
def automatic_fill():
    time.sleep(0.5)
    add_button.click()
    actual_number_of_rows = len(driver.find_elements(By.XPATH, "//tr[@class='eachRow']"))
    next_row_cells = driver.find_elements(By.XPATH,
                                          f"//table[@class='table table-bordered']/tbody/tr[{actual_number_of_rows}]/td/input")
    for i in range(len(list)):
        next_row_cells[i].clear()
        next_row_cells[i].send_keys(list[i])


# hány sort kell feltölteni
def repeater(number_of_rows_to_fill):
    for i in range(number_of_rows_to_fill):
        automatic_fill()


repeater(need_to_fill_row)

# feltöltést követően a kezdeti sorok száma megnövekszik a feltöltött sorok számával
assert len(driver.find_elements(By.XPATH, "//tr[@class='eachRow']")) == start_number_of_rows + need_to_fill_row

# TC2 : Keresés mező tesztelése
driver.get(URL)

test_data = "basketball"

number_of_test_data = len(driver.find_elements(By.XPATH, f"//input[@value='{test_data}']"))
search = driver.find_element(By.XPATH, "//input[@type='text' and @placeholder='Search...']")
search.send_keys(test_data)

assert number_of_test_data == len(driver.find_elements(By.XPATH, "//tr[@class='eachRow']"))
time.sleep(1)

# TC3 : Sorok törlése a táblázatból
driver.get(URL)
time.sleep(1)

# cheatsheet
# # xpath-to-some-element//parent::<tag>
# # xpath-to-some-element//following-sibling::<tag>

# list_of_electronics = driver.find_elements(By.XPATH, "//input[@value='Electronics']")

# az Electronics kategóriájú termékek törlés, azaz X gombjainak listába gyűjtése
list_of_buttons_electronics = driver.find_elements(By.XPATH, "//input[@value='Electronics']/parent::td//following-sibling::td/input")

# minden gombot az előbb kikeresett listából sorban megkattintunk, azaz minden Electronics terméket törlünk
for element in list_of_buttons_electronics:
    element.click()
    time.sleep(1)

# törlést követően nem lesz Electronics kategóriájú termék
assert len(driver.find_elements(By.XPATH, "//input[@value='Electronics']")) == 0

driver.close()
