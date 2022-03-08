# Python con selenium
## ¿Qué es Selenium o Selenium WebDriver?

Con el fin de ahorrar tiempo y costes al desarrollar aplicaciones en Python, Jason Huggins creó en 2004 el **JavaScriptTestRunner**, el núcleo del marco de trabajo de pruebas de web que ahora se conoce como Selenium. Al principio, la herramienta se utilizaba solo de forma interna en la empresa de _software_** ThoughtWorks,** donde Huggins trabajaba en ese momento. Cuando se cambió a **Google** en 2007, Huggins continuó desarrollando y perfeccionando el programa, que pasó a ser de código abierto (licencia Apache 2.0) y, por lo tanto, se puso a disposición del gran público. Después de **fusionarse con la API WebDriver,** el marco de pruebas recibió el nombre de Selenium o Selenium WebDriver, que sigue vigente hoy en día.

## Primer programa

El siguiente programa importa el webdriver de  Selenium en Python para automatizar pruebas/procesos web, en este caso se trabaja con el navegador chrome, por ello es  necesario descargar el archivo .exe del webdriver segun la version que se requiera, luego poner el exe en una ruta especifica para que en el parametro **executable_path** pongas la ruta, ejemplo: este programa ingresa a las webs y toma capturas de pantalla.

```python
from selenium import webdriver
import time

driver = webdriver.Chrome(
    executable_path=r"E:\apuntes\bots\python\documentacion\driver\99\chromedriver.exe")

web =[
    'http://python.org',
    'https://organitiempo.com/',
    'https://stackoverflow.com/'
]

for i in range(0,len(web)):
    driver.get(web[i])
    driver.get_screenshot_as_file(
        "E:\\apuntes\\bots\\python\\documentacion\\primer programa\\"+"shoot"+str(i)+".png")
    print(driver.title)
    time.sleep(1)
driver.quit()

```

## ¿Como hacer click ?

Para hacer click en algun elemento de una pagina web es importante tener conocimiento de la estructura de las paginas web, por ejemplo dentro de las paginas webs podemos tener diferentes elementos como botones, combos, cajas de texto, etc ,  estos elementos tienen id el cual debe ser unico (no siempre) o pertenecen a un clase,  también los podemos identificar con xpath  luego de encontrar la forma de  identificar un elemento en una pagina web  ya podemos realizar diferentes acciones como dar click, el siguiente ejemplo da click un un boton mediante el xpath para identifcar el boton.

```python
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
```

## Llenar caja de texto

```python
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
```

## Llenar área de texto

```python
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
```

## Obtener texto

```python
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
```

## Obtener enlaces

```python
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
```

## seleccionar Radio Button

```python
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
```

## seleccionar combo

```python
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
```



