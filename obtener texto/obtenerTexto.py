from selenium import webdriver
import time
import os

#iniciar webdriver y cargar pagina web de archivo local
driver = webdriver.Chrome(
    executable_path=r"E:\apuntes\bots\python\documentacion\driver\99\chromedriver.exe")

url = "file:///E:/apuntes/bots/python/documentacion/material/code/websites/element.html"
driver.get(url)
time.sleep(1)
#obtener texto del elemento title1
title1 = driver.find_element_by_id("title1").text
print(title1)
#obtener texto del elemento profile
linkText = driver.find_element_by_id("profile").text
print(linkText)

time.sleep(5)
driver.quit()