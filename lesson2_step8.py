from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    input1 = browser.find_element_by_xpath("//input[@name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@name='lastname']")
    input2.send_keys("Ivanov")
    input3 = browser.find_element_by_xpath("//input[@name='email']")
    input3.send_keys("qwer@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    browser.find_element_by_tag_name("button").click()
    alert = browser.switch_to.alert
    alert_text = alert.text

finally:
    time.sleep(10)
    browser.quit()
