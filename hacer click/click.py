from selenium import webdriver
import time
import os

driver = webdriver.Chrome(
    executable_path=r"E:\apuntes\bots\python\documentacion\driver\99\chromedriver.exe")

url = "file:///E:/apuntes/bots/python/documentacion/recursos/web/buttom.html"
driver.get(url)
time.sleep(1)

#boton click con xpath
python_button = driver.find_element_by_xpath('//*[@id="button"]')
python_button.click()

#cerrar alerta de navegador
time.sleep(1)
alert = driver.switch_to_alert()
alert.accept()

time.sleep(5)
driver.quit()