from .base_page import BasePage
from selenium.webdriver.common.by import By

class TowingTrailersCategoryPage(BasePage):

    #Locators

    loc_h1_towingTrailers_pTowing = (By.XPATH, '//h1[contains(text(), "Trailers and Tow Vehicles")]')

    def towing_trailers_title_displayed(self):
        towingTrailersTitle = self.driver.find_element(*TowingTrailersCategoryPage.loc_h1_towingTrailers_pTowing)
        return towingTrailersTitle.is_displayed()
