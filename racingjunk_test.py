import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

selHub = os.environ['SELHUB']
executor = 'http://'+ selHub + ':4444/wd/hub'



chrome = webdriver.Remote(
            command_executor=executor,
            desired_capabilities=DesiredCapabilities.CHROME)
firefox = webdriver.Remote(
            command_executor=executor,
            desired_capabilities=DesiredCapabilities.FIREFOX)

chrome.get('https://www.racingjunk.com')
print(chrome.title)

firefox.get('https://www.racingjunk.com')
print(firefox.title)

#Locators
mainLogoChrome= chrome.find_element_by_xpath("//div[@class='mainLogo']/a")
classifiedsMain= chrome.find_element_by_xpath("//li[@class='menu']/a[contains(text(),'Classifieds')]")

classifiedsMain.click()
try:
    element = chrome.find_element_by_xpath("//h1[@class='font12px'][contains(text(), 'Race, Drag')]")
except NoSuchElementException as exception:
    print("Element not found")








chrome.quit()
firefox.quit()
