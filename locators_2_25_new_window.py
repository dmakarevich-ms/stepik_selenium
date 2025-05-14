from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    browser = webdriver.Chrome(options)
    browser.get(link)

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
    window_tabs = browser.window_handles
    print(window_tabs)
    browser.switch_to.window(window_tabs[1])

    x_element = browser.find_element(By.ID, "input_value")
    x_element.get_attribute('value')
    x = x_element.text
    y = calc(x)
    fill_form = browser.find_element(By.XPATH, "//input[@id='answer']")
    fill_form.send_keys(y)
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()


finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()