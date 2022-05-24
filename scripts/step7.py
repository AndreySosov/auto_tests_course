import os
from selenium import webdriver
import time


link ="http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('.form-group>[name="firstname"')
    input1.send_keys("123")
    input2 = browser.find_element_by_css_selector('.form-group>[name="lastname"')
    input2.send_keys("123")
    input3 = browser.find_element_by_css_selector('.form-group>[name="email"')
    input3.send_keys("123")
    load_file = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    load_file.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn").click()
    # print(os.path.abspath(__file__))
    # print(os.path.abspath(os.path.dirname(__file__)))
finally:
    time.sleep(20)
    browser.quit()