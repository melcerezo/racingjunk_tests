from .base_page import BasePage
from selenium.webdriver.common.by import By

class DragRacingCarCategoryPage(BasePage):

    #Locators

    loc_h1_dragRacingTitle_pDrag = (By.XPATH, '//h1[contains(text(), "Drag Racing Cars")]')

    def drag_racing_car_title_displayed(self):
        dragRacingCarTitle = self.driver.find_element(*DragRacingCarCategoryPage.loc_h1_dragRacingTitle_pDrag)
        return dragRacingCarTitle.is_displayed()