from selenium import webdriver
import time
link = "http://suninjuly.github.io/selects1.html"
def sum_num(a,b):
    return str(a+b)
try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num1_int = int(num1.text)
    num2 = browser.find_element_by_id("num2")
    num2_int = int(num2.text)
    y = sum_num(num1_int, num2_int)
    select = browser.find_element_by_id("dropdown").click()
    elem = browser.find_element_by_css_selector(f'[value="{y}"]').click()
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(30)
    browser.quit()