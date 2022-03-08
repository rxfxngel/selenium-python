from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import os

#iniciar webdriver y cargar pagina web de archivo local
driver = webdriver.Chrome(
    executable_path=r"E:\apuntes\bots\python\documentacion\driver\99\chromedriver.exe")

url = "file:///E:/apuntes/bots/python/documentacion/material/code/websites/checkbox.html"
driver.get(url)
time.sleep(1)

#dar check
cbox = driver.find_element_by_xpath("/html/body/form/input[3]")
cbox.click()
time.sleep(2)

driver.quit()
