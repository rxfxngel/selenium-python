from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"E:\apuntes\bots\python\driver\99\chromedriver.exe")

web =[
    'http://python.org',
    'https://organitiempo.com/',
    'https://stackoverflow.com/'
]

for i in range(0,len(web)):
    driver.get(web[i])
    driver.get_screenshot_as_file("shoot"+str(i)+".png")
    print(driver.title)
    time.sleep(1)
driver.quit()

