from .base_page import BasePage
from selenium.webdriver.common.by import By

class EnginesCategoryPage(BasePage):

    #Locators

    loc_h1_engines_pEngines = (By.XPATH, '//h1[contains(text(), "Engines")]')

    def engines_title_displayed(self):
        enginesTitle = self.driver.find_element(*EnginesCategoryPage.loc_h1_engines_pEngines)
        return enginesTitle.is_displayed()