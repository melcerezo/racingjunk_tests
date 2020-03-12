from .base_page import BasePage
from selenium.webdriver.common.by import By

class OffRoadAndOverlandCategoryPage(BasePage):

    #Locators

    loc_h1_offRoadAndOverland_pOffRoad = (By.XPATH, '//h1[contains(text(), "Off-Road and Overland")]')
    
    def off_road_and_over_land_title_displayed(self):
        offRoadAndOverlandTitle = self.driver.find_element(*OffRoadAndOverlandCategoryPage.loc_h1_offRoadAndOverland_pOffRoad)
        return offRoadAndOverlandTitle.is_displayed()