import time
import getpass

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

pwd = getpass.getpass("Enter your password: ")

driver = webdriver.Chrome()

driver.get("https://tisoware.isc.loc")

dropdown_element = driver.find_element(By.NAME, "Company")
dropdown = Select(dropdown_element)
dropdown.select_by_index(0)

uid_input = driver.find_element(By.NAME, "UID")
uid_input.send_keys("sha79396")

pwd_input = driver.find_element(By.NAME, "PWD")
pwd_input.send_keys(pwd)

login_button = driver.find_element(By.NAME, "login")
login_button.click()

dropdown_element = driver.find_element(By.NAME, "tpinp")
dropdown = Select(dropdown_element)
dropdown.select_by_index(2)

dropdown_element = driver.find_element(By.NAME, "wt")
dropdown = Select(dropdown_element)
dropdown.select_by_index(1)

login_button = driver.find_element(By.ID, "save2")
login_button.click()

time.sleep(5)

print("Done")