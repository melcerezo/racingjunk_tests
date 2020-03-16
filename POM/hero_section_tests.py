import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pages import home_page, dirt_oval_racing_car_category_page, drag_racing_car_category_page
from pages import off_road_and_over_land_category_page, towing_trailers_category_page, engines_category_page

# Global set up
executor = 'http://localhost:4444/wd/hub'
URL = "https://www.racingjunk.com"

class ClickDragRacingCarsLink(unittest.TestCase):
    """Test case to click drag racing cars link"""

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor=executor,
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver.get(URL)

    def test_click_drag_racing_cars_link(self):
        homePage = home_page.HomePage(self.driver)
        homePage.click_drag_racing_cars()
        drag_cat_page = drag_racing_car_category_page.DragRacingCarCategoryPage(self.driver)
        assert drag_cat_page.drag_racing_car_title_displayed()

    def tearDown(self):
        self.driver.quit()

class ClickDirtOvalRacingCarsLink(unittest.TestCase):
    """Test case to click dirt oval racing cars link"""

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor=executor,
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver.get(URL)

    def test_click_dirt_oval_racing_cars_link(self):
        homePage = home_page.HomePage(self.driver)
        homePage.click_dirt_oval_racing_cars()
        dirt_cat_page = dirt_oval_racing_car_category_page.DirtOvalRacingCarCategoryPage(self.driver)
        assert dirt_cat_page.dirt_oval_racing_car_title_displayed()

    def tearDown(self):
        self.driver.quit()

class ClickOffRoadAndOverlandLink(unittest.TestCase):
    """Test case to click off-road and over land link"""

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor=executor,
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver.get(URL)

    def test_click_off_road_and_over_land_link(self):
        homePage = home_page.HomePage(self.driver)
        homePage.click_off_road_and_over_land()
        off_road_cat_page = off_road_and_over_land_category_page.OffRoadAndOverlandCategoryPage(self.driver)
        assert off_road_cat_page.off_road_and_over_land_title_displayed()

    def tearDown(self):
        self.driver.quit()

class ClickTowingTrailersLink(unittest.TestCase):
    """Test case to click towing trailer link"""

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor=executor,
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver.get(URL)

    def test_click_towing_trailers_link(self):
        homePage = home_page.HomePage(self.driver)
        homePage.click_towing_trailers()
        tow_trailers_cat_page = towing_trailers_category_page.TowingTrailersCategoryPage(self.driver)
        assert tow_trailers_cat_page.towing_trailers_title_displayed()

    def tearDown(self):
        self.driver.quit()

class ClickEnginesLink(unittest.TestCase):
    """Test case to click engine link"""

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor=executor,
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver.get(URL)

    def test_click_engines_link(self):
        homePage = home_page.HomePage(self.driver)
        homePage.click_engines()
        engines_cat_page = engines_category_page.EnginesCategoryPage(self.driver)
        assert engines_cat_page.engines_title_displayed()
    
    def tearDown(self):
        self.driver.quit()