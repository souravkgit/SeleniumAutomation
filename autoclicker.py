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
    driver1 = webdriver.Firefox()
    driver = webdriver.Firefox()
    driver1.get("https://www.temporary-mail.net/")
    print("Opening mail site....")
    driver.get(link)
    print("Opening your link....")
    sleep(5)
    print("Fetching temporary mail...")
    email = driver1.find_element_by_css_selector("input[type='text']").get_attribute("value")
    print("Mail fetched successfully...")
    sleep(2)
    driver.find_element_by_link_text('Log In / Register').click()
    sleep(1)
    driver.find_element_by_css_selector("input[type='text']").send_keys(email)
    print("Entering mail....")
    sleep(1)
    driver.find_element_by_class_name("r-adyw6z").click()
    print("Waiting for otp...")
    sleep(50)

    print("Fetching recieved mail...")
    venue = WebDriverWait(driver1, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="link open"]')))
    link = venue.get_attribute('href')
    driver2 = webdriver.Firefox()
    driver2.get(link)
    sleep(10)
    driver1.close()
    print("Getting otp...")
    text1 = driver2.find_elements_by_xpath("//span")
    for el in text1:
        if (len(el.text)==6):
            otp = el.text
    print("OTP fetched successfully....")
    list1 = driver.find_elements_by_css_selector("input[type='text']")
    i = 0
    print("Entering otp....")
    for el in list1:
        el.send_keys(otp[i])
        i += 1
        sleep(2)
    print("refer successfull...")
    sleep(5)
    driver.close()
    driver2.close()
    print("doing one more refer....")

















# xpath = '//a[@class="ng-binding"]'
# wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
# links = [venue.get_attribute('href') for venue in driver.find_elements_by_xpath(xpath)]

# for link in links:
#     driver.get(link)
#     hours = driver.find_element_by_xpath('//li[@id="hours"]')
#     hours.click()
#     hoursTable = driver.find_elements_by_css_selector("table.opening-times tr")
#     for row in hoursTable:
#         print(row.text)