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

    def user_name_field_displayed(self):
        userNameField = self.driver.find_element(*LoginPage.loc_input_userNameField_pLogin)
        return userNameField.is_displayed()

    def password_field_displayed(self):
        passwordField = self.driver.find_element(*LoginPage.loc_input_passwordField_pLogin)
        return passwordField.is_displayed()

    def forgot_username_displayed(self):
        forgotUsername = self.driver.find_element(*LoginPage.loc_a_forgotUsername_pLogin)
        return forgotUsername.is_displayed()

    def forgot_password_displayed(self):
        forgotPassword = self.driver.find_element(*LoginPage.loc_a_forgotPassword_pLogin)
        return forgotPassword.is_displayed

    