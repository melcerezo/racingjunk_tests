from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    #Locators

    loc_img_loginHeader_pLogin = (By.XPATH, '//div[@id="mainContent"]//img[@alt="Already A Member"]')
    loc_input_userNameField_pLogin = (By.XPATH, '//table[@class="loginTable"]//input[@name="username"]')
    loc_input_passwordField_pLogin = (By.XPATH, '//table[@class="loginTable"]//input[@name="password"]')
    loc_input_loginButton_pLogin = (By.XPATH, '//table[@class="loginTable"]//input[@type="submit"]')
    loc_a_forgotUsername_pLogin = (By.XPATH, '//table[@class="loginTable"]//a[@href="/user_lookup"]')
    loc_a_forgotPassword_pLogin = (By.XPATH, '//table[@class="loginTable"]//a[@href="/forgot_password"]')

    #Verify Displayed Function

    def login_header_displayed(self):
        loginHeader = self.driver.find_element(*LoginPage.loc_img_loginHeader_pLogin)
        return loginHeader.is_displayed()