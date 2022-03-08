from selenium import webdriver
import time
import os

#iniciar webdriver y cargar pagina web de archivo local
driver = webdriver.Chrome(
    executable_path=r"E:\apuntes\bots\python\documentacion\driver\99\chromedriver.exe")

url = "file:///E:/apuntes/bots/python/documentacion/material/code/websites/textbox.html"
driver.get(url)
time.sleep(1)

# enter text
field1 = driver.find_element_by_id("textbox")
field1.send_keys('Hola mundo\nRafael\nMamani')
time.sleep(1)

#close  browser

time.sleep(5)
driver.quit()
