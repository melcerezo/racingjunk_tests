import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import page

class ClickDirtOvalRacingCarsLink(unittest.TestCase):
    """Test case to click dirt oval racing cars link"""

    def setUp(self):
        self.selHub = 'localhost'
        self.executor = 'http://' + self.selHub + ':4444/wd/hub'
        self.driver = webdriver.Remote(
            command_executor=self.executor,
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver.get("https://www.racingjunk.com")

    def test_click_dirt_oval_racing_cars_link(self):
        home_page = page.HomePage(self.driver)
        home_page.click_dirt_oval_racing_cars()
        dirt_cat_page = page.DirtOvalRacingCarCategoryPage(self.driver)
        assert dirt_cat_page.dirt_oval_racing_car_title_displayed()

    def tearDown(self):
        self.driver.save_screenshot('dirt_screen.png')
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
