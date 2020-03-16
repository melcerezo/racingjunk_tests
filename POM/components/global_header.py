from .base_component import BaseComponent
from selenium.webdriver.common.by import By

class GlobalHeaderComponent(BaseComponent):

    #Locators

    loc_header_headerSection_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]')
    loc_a_imageLogo_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//a[@href="/"]')
    loc_a_loginLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//a[contains(text(), "Log In")]')
    loc_a_registerLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//a[contains(text(), "Register")]')
    loc_btn_postAdButton_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav/a[@class="btnPostAd"]')

    #Verify Displayed Functions

    def image_logo_displayed(self):
        imageLogo = self.driver.find_element(*GlobalHeaderComponent.loc_a_imageLogo_cGlobalHeader)
        return imageLogo.is_displayed()

    def login_link_displayed(self):
        loginLink = self.driver.find_element(*GlobalHeaderComponent.loc_a_loginLink_cGlobalHeader)
        return loginLink.is_displayed()
    
    def register_link_displayed(self):
        registerLink = self.driver.find_element(*GlobalHeaderComponent.loc_a_registerLink_cGlobalHeader)
        return registerLink.is_displayed()

    def post_ad_button_displayed(self):
        postAdButton = self.driver.find_element(*GlobalHeaderComponent.loc_btn_postAdButton_cGlobalHeader)
        return postAdButton.is_displayed()

    #Click Functions

    def click_image_logo(self):
        imageLogo = self.driver.find_element(*GlobalHeaderComponent.loc_a_imageLogo_cGlobalHeader)
        imageLogo.click()

    def click_login_link(self):
        loginLink = self.driver.find_element(*GlobalHeaderComponent.loc_a_loginLink_cGlobalHeader)
        loginLink.click()
    
    def click_register_link(self):
        registerLink = self.driver.find_element(*GlobalHeaderComponent.loc_a_registerLink_cGlobalHeader)
        registerLink.click()

    def click_post_ad_button(self):
        postAdButton = self.driver.find_element(*GlobalHeaderComponent.loc_btn_postAdButton_cGlobalHeader)
        postAdButton.click()

    

