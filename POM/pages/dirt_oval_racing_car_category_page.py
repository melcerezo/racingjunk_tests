from .base_page import BasePage
from selenium.webdriver.common.by import By

class DirtOvalRacingCarCategoryPage(BasePage):

    #Locators

    loc_h1_dirtOvalRacingTitle_pDirt = (By.XPATH, '//h1[contains(text(), "Dirt Oval Racing Cars")]')

    def dirt_oval_racing_car_title_displayed(self):
        dirtOvalRacingCarTitle = self.driver.find_element(*DirtOvalRacingCarCategoryPage.loc_h1_dirtOvalRacingTitle_pDirt)
        return dirtOvalRacingCarTitle.is_displayed()