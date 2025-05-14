from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button_on_page(browser):
    browser.get(link)
    time.sleep(20)
    add_cart_button = browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert add_cart_button.is_displayed(), f"Button not located on page"

