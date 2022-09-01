# importok
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# oldal megnyitása
driver.get("http://selenium.oktwebs.training360.com/r2d2_felezovizsga/coin_flip.html")

# elemek kikeresése
money = driver.find_element(By.ID, "cash")
bet = driver.find_element(By.ID, "bet")
result = driver.find_element(By.ID, "outcome")
tails_btn = driver.find_element(By.ID, "tails")
heads_btn = driver.find_element(By.ID, "heads")

# print(money.get_attribute("value"))
# print(bet.get_attribute("value"))
# print(result.text)

# TC_000
try:
    assert money.get_attribute("value") == "100"
    assert bet.get_attribute("value") == ""
    assert result.text == "-"
    print("TC_000 passed!")
except:
    print("TC_000 failed!")

print("=" * 40)

# bet.send_keys("10")
# tails_btn.click()
# print(result.text)
# if result.text == "tails":
#     assert money.get_attribute("value") == "110"
#     print("nyert")
# else:
#     assert money.get_attribute("value") == "90"
#     print("bukta")

# TC_001
try:
    bet.send_keys("10")
    tails_btn.click()
    if result.text == "tails":
        assert money.get_attribute("value") == "110"
        print("Your bet was TAILS, result is: " + result.text + " => You win!")
    else:
        assert money.get_attribute("value") == "90"
        print("Your bet was TAILS, result is: " + result.text + " => You lose!")
    print("TC_001 passed!")
except:
    print("TC_001 failed!")

driver.close()
