"""importok"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

"""driver létrehozása"""
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


try:
    driver.get("http://selenium.oktwebs.training360.com/sl10_proba_zarovizsga/film_register.html")
    time.sleep(3)

    # TC1: a filmek listába gyűjtése

    movies_number = driver.find_elements(By.CLASS_NAME, "container-movies")
    assert len(movies_number) == 24

    # TC2: az opciók listába gyűjtése

    nr_of_options = driver.find_elements(By.TAG_NAME, 'option')
    assert len(nr_of_options) == 3


    # TC3:
    #listába rendezett webelement id-k és tesztadatok
    ids = ["nomeFilme", "anoLancamentoFilme", "anoCronologiaFilme", "linkTrailerFilme", "linkImagemFilme",
           "linkImdbFilme"]
    test_data = ["Black widow", "2021", "2020", "https://www.youtube.com/watch?v=Fp9pNPdNwjI",
                 "https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg",
                 "https://www.imdb.com/title/tt3480822/"]

    register_button = driver.find_element(By.CLASS_NAME, "mostra-container-cadastro")
    register_button.click()
    time.sleep(2)

    #beviteli mező kitöltése függvénybe szervezve
    def find_and_send(id, data):
        driver.find_element(By.ID, id).send_keys(data)

    #a listába rendezett adatokon iterálás
    for i in range(len(test_data)):
        find_and_send(ids[i], test_data[i])

    save_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/fieldset/button[1]")
    save_button.click()

    #filmek újbóli listába gyűjtése
    movies_number_after_new_reg = driver.find_elements(By.CLASS_NAME, "container-movies")
    assert len(movies_number_after_new_reg) == 25
    time.sleep(2)

finally:
    driver.close()