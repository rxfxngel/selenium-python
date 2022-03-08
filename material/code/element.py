from selenium import webdriver
import time
import os

# start webdriver and load website from disk
driver = webdriver.Firefox()
url = 'file:///' + os.getcwd() + '/websites/element.html'
driver.get(url)
time.sleep(1)
 
# get element text
print( driver.find_element_by_id("title1").text )
print( driver.find_element_by_id("title2").text )
print( driver.find_element_by_id("text1").text )
print( driver.find_element_by_id("text2").text )
print( driver.find_element_by_id("profile").text )



time.sleep(5)
driver.quit()

