from .base_component import BaseComponent
from selenium.webdriver.common.by import By

class GlobalHeaderComponent(BaseComponent):

    #Locators

    loc_header_headerSection_cGlobalHeader = (By.ID, 'mainHeader') 
    loc_a_imageLogo_cGlobalHeader = (By.CSS_SELECTOR, '#mainHeader .mainLogo a')
    loc_a_loginLink_cGlobalHeader = (By.CSS_SELECTOR, '#mainHeader ul.loggedOutNav a[href*="user_login"]')
    loc_a_registerLink_cGlobalHeader = (By.CSS_SELECTOR, '#mainHeader ul.loggedOutNav a[href*="signup"]')
    
    # Nav Locators
    
    loc_a_navClassifiedsMenu_cGlobalHeader = (By.CSS_SELECTOR 'li.menu a[data-gaclick="MainNavDrop|Browse"]')
    loc_a_navMostRecentAdsLink_cGlobalHeader = (By.CSS_SELECTOR, 'nav ul li a[data-gaclick="MainNavDrop|Most Recent"]')
    loc_a_navNewsTechMenu_cGlobalHeader = (By.CSS_SELECTOR, 'li.menu a[data-gaclick="MainNavDrop|News"]')
    loc_a_navEventsMenu_cGlobalHeader = (By.CSS_SELECTOR, 'li.menu a[href="/events"]')
    loc_a_navForumLink_cGlobalHeader = (By.CSS_SELECTOR, 'li.menu a[href="/forums"]')
    loc_a_navPartnersLink_cGlobalHeader = (By.CSS_SELECTOR, 'nav ul li a[data-gaclick="MainNavDrop|Partners"]')
    loc_a_navDirectoryLink_cGlobalHeader = (By.CSS_SELECTOR, 'nav ul li a[data-gaclick="MainNavDrop|Dealer Directory"]')
    loc_a_navStoreLink_cGlobalHeader = (By.CSS_SELECTOR, 'nav ul li a[data-gaclick="MainNavDrop|Store"] ')
    loc_btn_postAdButton_cGlobalHeader = (By.CSS_SELECTOR, 'nav a.btnPostAd')
    
    # Classifieds Sub Menu Locators
    
    loc_a_subMenuClassifiedsCategoriesLink_cGlobalHeader = (By.CSS_SELECTOR, 'li.menu ul.menu li a[data-gaclick="SubNavDrop|Categories"]')
    loc_a_subMenuClassifiedsAdvancedSearchLink_cGlobalHeader = (By.CSS_SELECTOR, 'li.menu ul.menu li a[data-gaclick="SubNavDrop|Search"]')
    loc_a_subMenuClassifiedsAdsByDayLink_cGlobalHeader = (By.CSS_SELECTOR, 'li.menu ul.menu li a[data-gaclick="SubNavDrop|Ads By Day"]')
    loc_a_subMenuClassifiedsMostRecentAdsLink_cGlobalHeader = (By.CSS_SELECTOR, 'li.menu ul.menu li a[data-gaclick="SubNavDrop|Most Recent"]')
    loc_a_subMenuClassifiedsMostPopularAdsLink_cGlobalHeader = (By.CSS_SELECTOR, 'li.menu ul.menu li a[data-gaclick="SubNavDrop|Most Popular"]')
    
    # News Tech Sub Menu Locators
    
    loc_a_subMenuNewsTechCircleTrackLink_cGlobalHeader = (By.CSS_SELECTOR, 'li a[href="/news/category/circle-track-racing/"]')
    loc_a_subMenuNewsTechDirtTrackLink_cGlobalHeader = (By.CSS_SELECTOR, 'li a[href="/news/category/dirt-track-racing/"]')
    loc_a_subMenuNewsTechDragRacingLink_cGlobalHeader = (By.CSS_SELECTOR, 'li a[href="/news/category/drag-racing/"]')
    loc_a_subMenuNewsTechMotorcyclesLink_cGlobalHeader = (By.CSS_SELECTOR, 'li a[href="/news/category/motorcycles-and-powersports/"]')
    loc_a_subMenuNewsTechNHRALink_cGlobalHeader = (By.CSS_SELECTOR, 'li a[href="/news/category/nhra"]')
    loc_a_subMenuNewsTechNASCARLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/news/category/nascar/"]')
    loc_a_subMenuNewsTechOffRoadLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/news/category/off-road-racing/"]')
    loc_a_subMenuNewsTechOtherRacingLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/news/category/other-racing/"]')
    loc_a_subMenuNewsTechThrowBackThursdayLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/news/category/throwback-thursday/"]')
    loc_a_subMenuNewsTechTractorTruckLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/news/category/tractor-truck-pulling/"]')
    loc_a_subMenuNewsTechEventCoverageLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/news/category/event-coverage/"]')
    loc_a_subMenuNewsTechNewsLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/news"]')
    loc_a_subMenuNewsTechPressReleasesLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/news/category/product-news-releases/press-release/"]')
    loc_a_subMenuNewsTechProductNewsLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/news/category/product-news-releases/press-release/"]')
    loc_a_subMenuNewsTechCarShowsLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/news/tag/car-shows/"]')
    loc_a_subMenuNewsTechGalleriesEventCoverageLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/news/tag/event-coverage-2/"]')
    loc_a_subMenuNewsTechDragRace101Link_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/news/category/drag-race-101/"]')
    loc_a_subMenuNewsTechHowToTechLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/news/category/how-tos/"]')
    loc_a_subMenuNewsTechBuildOrBuyLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/news/tag/repair-or-replace/"]')
    loc_a_subMenuNewsTechCoolCarFindLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/news/tag/rj-cool-car-find/"]')
    loc_a_subMenuNewsTechFeaturedBuildsLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/news/category/featured-vehicles/"]')
    loc_a_subMenuNewsTechPinupLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/news/category/pinup/"]')
    
    # Event Sub Menu Locators
    
    loc_a_subMenuEventsUpcomingEventsLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/events/all-types"]')
    loc_a_subMenuEventsSubmitEventLink_cGlobalHeader = (By.XPATH, '//header[@id="mainHeader"]//nav//li[@class="menu"]//ul[contains(@class, "menu")]//a[@href="/events/create"]')

    # Search locators

    loc_form_searchBar_cGlobalHeader = (By.XPATH, '//form[contains(@class, "search")]')
    loc_select_searchSelectDropdown_cGlobalHeader = (By.XPATH, '//select[@id="searchCategorySelector"]')
    loc_input_searchInput_cGlobalHeader = (By.XPATH, '//input[@name="searchString"]')
    loc_a_searchSubmit_cGlobalHeader = (By.XPATH, '//a[@class="searchSubmit"]')



    #Verify Displayed Functions

    def image_logo_displayed(self):
        imageLogo = self.driver.find_element(*GlobalHeaderComponent.loc_a_imageLogo_cGlobalHeader)
        return imageLogo.is_displayed()

    def login_link_displayed(self):
        loginLink = self.driver.find_element(*GlobalHeaderComponent.loc_a_loginLink_cGlobalHeader)
        return loginLink.is_displayed()
    
    def register_link_displayed(self):
        registerLink = self.driver.find_element(*GlobalHeaderComponent.loc_a_registerLink_cGlobalHeader)
        return registerLink.is_displayed()

    def search_bar_displayed(self):
        searchBar = self.driver.find_element(*GlobalHeaderComponent.loc_form_searchBar_cGlobalHeader)
        return searchBar.is_displayed()

    def post_ad_button_displayed(self):
        postAdButton = self.driver.find_element(*GlobalHeaderComponent.loc_btn_postAdButton_cGlobalHeader)
        return postAdButton.is_displayed()

    #Click Functions

    def click_image_logo(self):
        imageLogo = self.driver.find_element(*GlobalHeaderComponent.loc_a_imageLogo_cGlobalHeader)
        imageLogo.click()

    def click_login_link(self):
        loginLink = self.driver.find_element(*GlobalHeaderComponent.loc_a_loginLink_cGlobalHeader)
        loginLink.click()
    
    def click_register_link(self):
        registerLink = self.driver.find_element(*GlobalHeaderComponent.loc_a_registerLink_cGlobalHeader)
        registerLink.click()

    def click_post_ad_button(self):
        postAdButton = self.driver.find_element(*GlobalHeaderComponent.loc_btn_postAdButton_cGlobalHeader)
        postAdButton.click()

    

