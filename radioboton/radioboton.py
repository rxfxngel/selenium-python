from selenium import webdriver
import time
import os

#iniciar webdriver y cargar pagina web de archivo local
driver = webdriver.Chrome(
    executable_path=r"E:\apuntes\bots\python\documentacion\driver\99\chromedriver.exe")

url = "file:///E:/apuntes/bots/python/documentacion/material/code/websites/radio.html"
driver.get(url)
time.sleep(1)

#select element
radio = driver.find_element_by_xpath("/html/body/form/input[3]")
radio.click()
time.sleep(2)

