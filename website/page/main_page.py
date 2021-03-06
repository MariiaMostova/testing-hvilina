from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.by import By

from website import assert_manager
from website.locator.main_page_locator import MainPageLocator
from website.page.base import Base


class MainPage(Base):

    def check(self):
        super().check()
        print('Main page opened')

    def catalog_menu_item_hover(self):
        self.hover(MainPageLocator.HEADER_MENU_ITEM_CATALOG)
        elem = self.driver_wait.until(visibility_of_element_located([By.XPATH, MainPageLocator.CATALOG_ITEM_FOR_HER]))
        assert_manager.assert_contains(elem.text, 'ДЛЯ НЕЇ')
        print('Catalog menu item hover')

    def for_her_catalog_item_click(self):
        old_url = self.driver.current_url
        self.click(MainPageLocator.CATALOG_ITEM_FOR_HER)
        new_url = self.driver.current_url
        assert_manager.assert_changed(old_url, new_url)
        print('For her catalog item clicked')

