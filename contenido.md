# Python con selenium
## ¿Qué es Selenium o Selenium WebDriver?

Con el fin de ahorrar tiempo y costes al desarrollar aplicaciones en Python, Jason Huggins creó en 2004 el **JavaScriptTestRunner**, el núcleo del marco de trabajo de pruebas de web que ahora se conoce como Selenium. Al principio, la herramienta se utilizaba solo de forma interna en la empresa de _software_** ThoughtWorks,** donde Huggins trabajaba en ese momento. Cuando se cambió a **Google** en 2007, Huggins continuó desarrollando y perfeccionando el programa, que pasó a ser de código abierto (licencia Apache 2.0) y, por lo tanto, se puso a disposición del gran público. Después de **fusionarse con la API WebDriver,** el marco de pruebas recibió el nombre de Selenium o Selenium WebDriver, que sigue vigente hoy en día.

## Primer programa

El siguiente programa importa en webdriver de  Selenium en Python para automatizar pruebas/procesos web, en este caso se trabaja con el navegador chrome, por ello es  necesario descargar el archivo .exe del webdriver segun la version que necesites, luego ponerlo en una ruta especifica para que en el parametro **executable_path** pongas la ruta, este programa ingresa a las webs y toma capturas de pantalla.

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

