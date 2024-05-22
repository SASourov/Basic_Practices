import random
import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

# Text box
name = driver.find_element(By.ID, "name")
name.send_keys("Automation Tester")
time.sleep(2)
driver.quit()

# JS ALERT HANDLING
jsAlert = driver.find_element(By.XPATH, "//button[text()='Prompt']")
jsAlert.click()
time.sleep(3)
driver.switch_to.alert.send_keys("Test Content")
time.sleep(3)
driver.switch_to.alert.accept()
time.sleep(5)

# Check and Radio Box
genderMale = driver.find_element(By.ID, "male")
genderMale.click()

genderFemale = driver.find_element(By.ID, "female")
genderFemale.click()

daysStatic = driver.find_element(By.ID, "monday")
daysStatic.click()

checkboxes = driver.find_elements(By.XPATH, "//input[@class='form-check-input' and @type='checkbox']")
for checkboxes in checkboxes:  # All Checkbox x
    checkboxes.click()
    checkboxes.click()
random_checkbox = random.choice(checkboxes)  # Random click
random_checkbox.click()

if checkboxes:  # LastOneClick
    checkbox = checkboxes[-1]
    checkbox.click()

if checkboxes:  # firstOneClick
    first_checkbox = checkboxes[0]
    first_checkbox.click()

# dropdown formula 1
countrySelect = Select(driver.find_element(By.ID, 'country'))
countrySelect.select_by_value("Canada")

# dropdown formula 2
countryArrowDown = driver.find_element(By.ID, 'country')
countryArrowDown.send_keys(Keys.ARROW_DOWN)
countryArrowDown.send_keys(Keys.ENTER)

date = driver.find_element(By.ID, "datepicker")
date.send_keys("2010/05/05")
date.send_keys(Keys.ENTER)

newWindow = driver.find_element(By.XPATH, "//button[text()='New Browser Window']")
newWindow.click()
driver.switch_to.window(driver.window_handles[1])
driver.switch_to.window(driver.window_handles[0])

doubleClick = driver.find_element(By.XPATH, "//button[text()='Copy Text']")
action = ActionChains(driver)
action.double_click(doubleClick).perform()
time.sleep(2)
