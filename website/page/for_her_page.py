from selenium.webdriver.common.by import By
from website.locator.for_her_page_locator import ForHerPageLocator
from website.page.base import Base
from selenium.webdriver.support.expected_conditions import *


class ForHerPage(Base):

    def check(self):
        super().check()
        print('For her page opened')

    def open_collections_filter_options(self):
        self.click(ForHerPageLocator.COLLECTIONS)
        self.driver_wait.until(visibility_of_element_located([By.XPATH, ForHerPageLocator.COLLECTIONS_OPTIONS]))
        print('Collections filter options are visible')

    def filter_by_narbut_collection(self):
        self.click(ForHerPageLocator.NARBUT_COLLECTIONS_FILTER_ITEM)
        self.driver_wait.until(visibility_of_element_located([By.XPATH, ForHerPageLocator.SELECTED_INDICATOR]))
        print('Products are filtered by Collections')

    def check_narbut_collection_checkbox(self):
        self.driver_wait.until(element_located_to_be_selected([By.XPATH, ForHerPageLocator.NARBUT_CHECKBOX]))
        print('Narbut option is selected')

    def add_narbut_carbon_black_to_favourite(self):
        self.get_favourite_counter()
        self.click(ForHerPageLocator.FAVOURITE_BUTTON)
        self.driver_wait.until(
            visibility_of_element_located([By.XPATH, ForHerPageLocator.ADDED_TO_FAVOURITE_INDICATOR]))
        assert self.driver_wait.until(
            text_to_be_present_in_element([By.XPATH, ForHerPageLocator.FAVOURITE_COUNTER], '1'))
        self.get_favourite_counter()
        print('Carbon Black Narbut os added to favourite')

    def get_favourite_counter(self):
        favourite_counter = self.get_element_by_xpath(ForHerPageLocator.FAVOURITE_COUNTER).get_attribute(
            "data-favorites-counter")
        print('Favourite counter:', favourite_counter)

    def open_narbut_silver_grey_page(self):
        product = ForHerPageLocator.NARBUT_SILVER_GREY_BLACK_PRODUCT
        self.click(product)
