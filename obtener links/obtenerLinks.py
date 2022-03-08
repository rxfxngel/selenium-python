from selenium import webdriver
import time
import os

#iniciar webdriver y cargar pagina web de archivo local
driver = webdriver.Chrome(
    executable_path=r"E:\apuntes\bots\python\documentacion\driver\99\chromedriver.exe")

url = "file:///E:/apuntes/bots/python/documentacion/material/code/websites/links.html"
driver.get(url)
time.sleep(1)

elems = driver.find_elements_by_xpath("//a[@href]")

for elem in elems:
    print(elem.get_attribute("href"))

driver.quit()