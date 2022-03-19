#! /usr/bin/python3
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common import action_chains
import unittest

link = "https://uplibra.io/?refer=1346492"

for i in range(100):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.temporary-mail.net/")
    # print(driver.title)
    sleep(5)
    print("Fetching temporary mail...")
# 		email = driver.find_element(By.ID,"active-mail").get_attribute("value")
    email = driver.find_element(
        By.CSS_SELECTOR, "input[id='active-mail']").get_attribute("value")
    print("Mail fetched successfully...")
    # print(email)
    driver.execute_script("window.open('');")
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    sleep(1)
    print("Opening your link...")
    driver.get(link)
    # sleep(5)
    # print(driver.title)
    
    sleep(2)
    driver.find_element(
        By.XPATH, '//a[@id="kt_login_signup"]').click()
    sleep(2)
    name = "sourav" + f"00{i}"
    password = "Goyalbrothers@3"
    driver.find_element(By.CSS_SELECTOR, "input[name='fullname']").send_keys(
        name)
    sleep(2)
    # passw = driver.find_elements(By.CLASS_NAME,"input[type='password']")
    sleep(1)
    # driver.find_elements(By.NAME,'rpassword')[0].send_keys(password)
    passw = driver.find_elements(By.CSS_SELECTOR, "input[type='password']")
    sleep(2)
    # for el in passw:
    #     el.send_keys(password)
    #     sleep(1)
    passw[1].send_keys(password)
    sleep(1)
    passw[2].send_keys(password)
    sleep(5)
    # driver.find_element(By.CSS_SELECTOR, "input[name='agree']").click()
    # driver.find_element(By.CSS_SELECTOR,'label[class="kt-checkbox"]').click()
    # tos_checkbox = driver.find_elements(By.XPATH,"//label[@class='kt-checkbox']/./..")
    # print(tos_checkbox)
    # tos_checkbox[1].click()

    # checkbox = webdriver.Wait(driver,10)driver.find_element_by_css_selector("label[class='kt-checkbox']")
    checkbox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "label[class='kt-checkbox']"))
    )
    checkbox.click()
    # action = action_chains.ActionChains(driver)
    # action.move_to_element_with_offset(checkbox, 1, 1).click().perform()

    sleep(4)
    driver.find_element(By.CSS_SELECTOR, "button[type='button']").click()
    sleep(20)
    print("Entering mail....")

    driver.find_element(
        By.CSS_SELECTOR, "input[type='text']").send_keys(email)
    print("Submitting...")
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "button[text='Submit']").click()
    sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    sleep(7)
    driver.refresh()
    sleep(2)
    print("Fetching recieved mail...")
    venue = driver.find_element(By.XPATH, '//a[@class="link open"]')
    linki = venue.get_attribute('href')
    driver.get(linki)
    sleep(3)
    venue2 = driver.find_elements(By.XPATH, '//a[@rel="nofollow"]')
    link2 = venue2[1].get_attribute('href')
    # print(link2)
    driver.get(link2)
    sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    sleep(1)
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    print(f"\n{i+1} Done!\n")


