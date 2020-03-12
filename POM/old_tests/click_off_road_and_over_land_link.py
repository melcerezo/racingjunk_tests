import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import page

class ClickOffRoadAndOverlandLink(unittest.TestCase):
    """Test case to click off-road and over land link"""

    def setUp(self):
        self.selHub = 'localhost'
        self.executor = 'http://' + self.selHub + ':4444/wd/hub'
        self.driver = webdriver.Remote(
            command_executor=self.executor,
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver.get("https://www.racingjunk.com")

    def test_click_off_road_and_over_land_link(self):
        home_page = page.HomePage(self.driver)
        home_page.click_off_road_and_over_land()
        off_road_cat_page = page.OffRoadAndOverlandCategoryPage(self.driver)
        assert off_road_cat_page.off_road_and_over_land_title_displayed()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()