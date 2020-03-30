import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from components import global_header
from pages import login_page, home_page

#Global setup
executor = 'http://localhost:4444/wd/hub'
URL = "https://www.racingjunk.com"

class ClickImageLogo(unittest.TestCase):
    """Test case to click Image logo in header"""

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor=executor,
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver.get(URL)

    def test_click_image_logo(self):
        globalHeader = global_header.GlobalHeaderComponent(self.driver)
        homePage = home_page.HomePage(self.driver)
        try:
            globalHeader.image_logo_displayed()
            globalHeader.click_image_logo()
            assert homePage.main_featured_content_displayed()
        except NoSuchElementException:
            print("Element is not visible")

    def tearDown(self):
        self.driver.quit()

class ClickLoginLink(unittest.TestCase):
    """Test case to click Login Link in header"""

    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor=executor,
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.driver.get(URL)

    def test_click_login_link(self):
        globalHeader = global_header.GlobalHeaderComponent(self.driver)
        loginPage = login_page.LoginPage(self.driver)
        try:
            globalHeader.login_link_displayed()
            globalHeader.click_login_link()
            assert loginPage.login_header_displayed()
        except NoSuchElementException:
            print("Element is not visible")

