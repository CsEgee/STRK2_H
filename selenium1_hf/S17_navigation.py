# importok
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# driver meghívása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# oldal megnyitása
driver.get("http://selenium.oktwebs.training360.com/general.html")

# linkek kigyűjtése
# links = driver.find_elements(By.TAG_NAME, "a")
links = driver.find_elements(By.XPATH, '//html/body/header/small/a')

# texts = []
# for link in links:
#     text = link.get_attribute('href')
#     texts.append(text)
#     print(text)

# for link in links:
#     try:
#         link_in = link.get_attribute('href')
#         link.click()
#         link_out = driver.current_url
#         assert link_in == link_out
#         print("A " + link_in + " helyesen működik!")
#     except:
#       # link_in = link.get_attribute('href')
#         print("A " + link_in + " nem működik!")

def link_check(link_to_check, link_in):
    try:
        link_to_check.click()
        link_out = driver.current_url
        assert link_in == link_out
        print("A " + link_in + " link helyesen működik!")
    except:
        print("A " + link_in + " link nem működik!")


# linkek ellenőrzése
for link in links:
    link_url = link.get_attribute('href')
    link_check(link, link_url)

driver.close()

# Azzal egyszerűsítjük a feladatot, hogy elegendő a Jump to: szekcióban található 5 anchor végiglátogatása oda-vissza.
# Annyi kísérletezés legyen benne, hogy pl. a "phrasing" anchorhoz érve legyen egy visszaugrás az induló lapra.
# Ez persze két külön kódot jelent egy fájlon belül! Print utasításokkal érdemes láthatóvá tenni a navigációt.
