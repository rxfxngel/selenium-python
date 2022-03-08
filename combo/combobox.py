from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import os

#iniciar webdriver y cargar pagina web de archivo local
driver = webdriver.Chrome(
    executable_path=r"E:\apuntes\bots\python\documentacion\driver\99\chromedriver.exe")

url = "file:///E:/apuntes/bots/python/documentacion/material/code/websites/dropdown.html"
driver.get(url)
time.sleep(1)

select = Select(driver.find_element_by_id('country'))
time.sleep(2)
#seleccionar por texto visible
select.select_by_visible_text('Germany')

time.sleep(2)

#seleccionar por valor
select.select_by_value('5')

time.sleep(5)

driver.quit()
