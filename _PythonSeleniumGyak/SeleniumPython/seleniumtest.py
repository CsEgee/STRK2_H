from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://python.org")

q = driver.find_element_by_name("q")
q.send_keys("input")

submit = driver.find_element_by_name("submit")
submit.click()


# find element by
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("http://selenium.oktwebs.training360.com/trickybuttons.html")
#
#
# def add(p, q, pr):
#     product = driver.find_element_by_id("product")
#     quantity = driver.find_element_by_id("quantity")
#     price = driver.find_element_by_id("price")
#     add_button = driver.find_element_by_id("add")
#
#     product.clear()
#     quantity.clear()
#     price.clear()
#
#     product.send_keys(p)
#     quantity.send_keys(q)
#     price.send_keys(pr)
#
#     add_button.click()
#
#
# add("Ford", 1, 75000)
# add("Audi", 1, 120000)


# több elem kigyűjtése egy kéréssel
# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# try:
#     driver.get("http://selenium.oktwebs.training360.com/trickybuttons.html")
#
#     buttons = driver.find_elements_by_xpath('//button')
#     print(buttons)
#     print(type(buttons))
#
#     for button in buttons:
#         button.click()
#         result = driver. find_element_by_xpath('//labell@id="result"]')
#         print(result.text)
#         assert(result.text == f"{button.text} was clicked")
# finally:
#     driver.close()
