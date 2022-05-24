import time
from selenium import webdriver
import math

link = "http://suninjuly.github.io/execute_script.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)
    valuex = browser.find_element_by_css_selector("label>#input_value")
    get_value_x = int(valuex.text)
    y = calc(get_value_x)
    input1 = browser.find_element_by_id("answer").send_keys(y)

    # assert people_checked == "true", "People radio is not selected by default"
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = browser.find_element_by_id("robotCheckbox").click()
    radiobutton = browser.find_element_by_id("robotsRule").click()
    button.click()
finally:
    time.sleep(30)
    browser.quit()
    print(get_value_x)

