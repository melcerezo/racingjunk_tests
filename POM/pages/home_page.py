from .base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    # Locators

    loc_div_featuredContent_pHome = (By.ID, 'mainContentFeatured')
    loc_a_dragRacingCars_pHome = (By.XPATH, '//div[@class="browseCategories"]//a[@href="/category/1/Drag-Racing-Cars.html"]')
    loc_a_dirtOvalRacingCars_pHome = (By.XPATH, '//div[@class="browseCategories"]//a[@href="/category/Dirt-Oval-Racing-Cars/2"]')
    loc_a_offRoadAndOverland_pHome = (By.XPATH, '//div[@class="browseCategories"]//a[@href="/category/Off-Road-and-Overland/1119"]')
    loc_a_towingTrailers_pHome = (By.XPATH, '//div[@class="browseCategories"]//a[@href="/category/Trailers-and-Tow-Vehicles/13"]')
    loc_a_engines_pHome = (By.XPATH, '//div[@class="browseCategories"]//a[@href="/category/Engines/6"]')
    loc_a_hotRodStreetRod_pHome = (By.XPATH, '//div[@class="browseCategories"]//a[@href="/category/1010/Hot-Rod-Street-Rod-Custom.html"]')
    loc_a_transmissionAndClutches_pHome = (By.XPATH, '//div[@class="browseCategories"]//a[@href="/category/1256/Transmissions-and-Clutches.html"]')

    def click_drag_racing_cars(self):
        dragRacingCarsButton = self.driver.find_element(*HomePage.loc_a_dragRacingCars_pHome)
        dragRacingCarsButton.click()

    def click_dirt_oval_racing_cars(self):
        dirtOvalRacingCarsButton = self.driver.find_element(*HomePage.loc_a_dirtOvalRacingCars_pHome)
        dirtOvalRacingCarsButton.click()

    def click_off_road_and_over_land(self):
        offRoadAndOverlandButton = self.driver.find_element(*HomePage.loc_a_offRoadAndOverland_pHome)
        offRoadAndOverlandButton.click()

    def click_towing_trailers(self):
        towingTrailersButton = self.driver.find_element(*HomePage.loc_a_towingTrailers_pHome)
        towingTrailersButton.click()