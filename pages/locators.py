from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():

    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_USER_MAIL = (By. NAME, 'login-username')
    PASS_TO_LOGIN = (By.NAME, "login-password")
    LOGIN_BUTTON = (By.NAME, 'login_submit')
    REGISTRATION_FORM = (By.ID, 'register_form')
    REGISTER_USER_MAIL = (By.NAME, 'registration-email')
    PASS_TO_REGISTR = (By.ID, 'id_registration-password1')
    REPEAT_PASS_TO_REGISTER =(By.ID, 'id_registration-password2')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')

