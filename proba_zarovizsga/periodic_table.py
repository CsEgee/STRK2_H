# importok
import filecmp

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

text = ''

try:

    # oldal megnyitása
    driver.get('http://selenium.oktwebs.training360.com/sl10_proba_zarovizsga/periodic_table.html')

    # elemek kigyűjtése listába
    values = []
    elements = driver.find_elements(By.XPATH, '/html/body/div/ul/li')
    element_number = len(elements)

    for i in range(element_number):
            if str(driver.find_element(By.XPATH, f'/html/body/div/ul/li[{i + 1}]').get_attribute('class')) == 'empty':
                pass
            else:
                element_pos = driver.find_element(By.XPATH, f'/html/body/div/ul/li[{i + 1}]').get_attribute('data-pos')
                element_name = driver.find_element(By.XPATH, f'/html/body/div/ul/li[{i + 1}]/span').text
                values.append(f'{element_pos}, {element_name}')

    print(values)

    # elemek kiírása fájlba
    with open('data_out.txt', 'w') as f:
        for value in values:
            f.write("%s\n" % value)
    f.close()

    file_in = 'data.txt'
    file_out = 'data_out.txt'

    assert filecmp.cmp(file_in, file_out)

finally:
    driver.close()
