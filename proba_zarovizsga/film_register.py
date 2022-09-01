# importok
import time
from selenium.webdriver.support.ui import Select


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:

    # oldal megnyitása
    driver.get('http://selenium.oktwebs.training360.com/sl10_proba_zarovizsga/film_register.html')

    # TC1 betöltés után megjelenő filmek száma
    time.sleep(3)
    film_counter = driver.find_elements(By.XPATH, '/html/body/div[2]/div[3]/a')
    film_count = len(film_counter)
    print(film_count)
    assert film_count == 24
    print('TC1 pass')

    # TC2 sorbarendezési módok
    select = Select(driver.find_element(By.XPATH, '//select[@id="ordenarFilmes"]'))

    select.select_by_value('nome')
    assert driver.find_element(By.XPATH, '//*[@id="ordenarFilmes"]/option[1]').text == 'Name'
    time.sleep(1)

    select.select_by_value('anoLancamento')
    assert driver.find_element(By.XPATH, '//*[@id="ordenarFilmes"]/option[2]').text == 'Launch'
    time.sleep(1)

    select.select_by_value('anoCronologico')
    assert driver.find_element(By.XPATH, '//*[@id="ordenarFilmes"]/option[3]').text == 'Chronology'
    time.sleep(1)

    print('TC2 pass')

    # TC3 új film felvitele
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/button').click()
    time.sleep(2)
    driver.find_element(By.ID, 'nomeFilme').send_keys('Black Widow')
    driver.find_element(By.ID, 'anoLancamentoFilme').send_keys('2021')
    driver.find_element(By.ID, 'anoCronologiaFilme').send_keys('2020')
    driver.find_element(By.ID, 'linkTrailerFilme').send_keys('https://www.youtube.com/watch?v=Fp9pNPdNwjI')
    driver.find_element(By.ID, 'linkImagemFilme').send_keys('https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg')
    driver.find_element(By.ID, 'linkImdbFilme').send_keys('https://www.imdb.com/title/tt3480822/')
    driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/fieldset/button[1]').click()
    time.sleep(2)

    # új film létrejöttének ellenőrzése (darabszám alapján)
    film_counter = driver.find_elements(By.XPATH, '/html/body/div[2]/div[3]/a')
    film_count = len(film_counter)
    print(film_count)
    assert film_count == 25
    print('TC3 pass')

finally:
    driver.close()
