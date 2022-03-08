from selenium import webdriver
import time
import os

#iniciar webdriver y cargar pagina web de archivo local
driver = webdriver.Chrome(
    executable_path=r"E:\apuntes\bots\python\documentacion\driver\99\chromedriver.exe")

url="file:///E:/apuntes/bots/python/documentacion/material/code/websites/textfields.html"
driver.get(url)
time.sleep(1)

#Ingresar nombre
field1=driver.find_element_by_id("FirstName")
field1.send_keys('Rafael')
time.sleep(1)

#Ingresar apellido
field1=driver.find_element_by_id("LastName")
field1.send_keys('Mamani')
time.sleep(1)

#close browser
time.sleep(5)
driver.quit()