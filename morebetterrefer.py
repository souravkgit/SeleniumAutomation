#! /usr/bin/python3

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import unittest 

count = int(input("Enter how many referells you want = "))
link = input("Enter your refrell link here : ")
for i in range(count):
    print("Opening mail site....")
    driver1 = webdriver.Firefox()
    print("Opening your link....")
    driver = webdriver.Firefox()
    driver1.get("https://www.temporary-mail.net/")
    driver.get(link)
    sleep(5)
    print("Fetching temporary mail...")
    email = driver1.find_element(By.CSS_SELECTOR,"input[type='text']").get_attribute("value")
    print("Mail fetched successfully...")
    sleep(2)
    driver.find_element(By.LINK_TEXT,'Log In / Register').click()
    sleep(1)
    driver.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys(email)
    print("Entering mail....")
    sleep(1)
    driver.find_element(By.CLASS_NAME,"r-adyw6z").click()
    print("Waiting for otp...")
    sleep(5)
    driver1.refresh()
    sleep(5)
    driver1.refresh()
    sleep(5)
    driver1.refresh()
    sleep(5)
    driver1.refresh()
    sleep(5)
    driver1.refresh()
    sleep(5)
    

    print("Fetching recieved mail...")
    venue = WebDriverWait(driver1, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="link open"]')))
    linki = venue.get_attribute('href')
    driver1.get(linki)
    sleep(10)
    elems = driver1.find_elements_by_xpath("//a[@href]")
    elem = elems[-3]
    link2 = elem.get_attribute("href")
    driver1.get(link2)
    sleep(15)
    print(f"refer done = {i+1}")
    if (i==count-1):
        print("\n\n\n***Thanks for using the tool , this tool is created by @souravkkk , give a special thanks to him on telegram.****\n\n\n")
    sleep(3)
    driver.close()
    driver1.close()
