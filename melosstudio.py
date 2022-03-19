#! /usr/bin/python3
from pyvirtualdisplay import Display
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import unittest 



# display = Display(visible=0, size=(800, 600))
# display.start()
count = int(input("Enter how many referells you want = "))
link = "https://www.melos.studio/registration?inviteCode=C86E0FC5"
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
    print("Entering mail....")
    driver.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys(email)
    print("Entering password...")
    driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("Goyalbrothers3")
    sleep(2)
    driver.find_element(By.CLASS_NAME,"circle").click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    sleep(5)
    driver1.refresh()
    sleep(3)
    print("Fetching recieved mail...")
    venue = WebDriverWait(driver1, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="link open"]')))
    linki = venue.get_attribute('href')
    driver1.get(linki)
    sleep(3)
    venue2 = driver1.find_elements(By.XPATH, '//a[@rel="nofollow"]')
    link2 = venue2[1].get_attribute('href')
    # print(link2)
    driver1.get(link2)
    sleep(2)
    driver.close()
    sleep(1)
    driver1.close()
    print(f"\n{i+1} Done!\n")
# display.stop()
    