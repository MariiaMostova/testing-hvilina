from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element

from website import assert_manager
from website.locator.cart_page_locator import CartPageLocator
from website.locator.narbut_carbon_black_locator import NarbutCarbonBlackLocator
from website.page.base import Base


class NarbutCarbonBlackPage(Base):

    def check(self):
        super().check()
        print('Narbut Carbon Black page opened')

    def get_cart_counter(self):
        cart_counter = self.get_element_by_xpath(CartPageLocator.CART_COUNTER).text
        print('Cart counter:', cart_counter)
        return cart_counter

    def add_to_cart(self):
        self.get_cart_counter()
        self.get_element_by_xpath(NarbutCarbonBlackLocator.ADD_TO_CART_BUTTON).click()
        self.driver_wait.until(
            text_to_be_present_in_element([By.XPATH, NarbutCarbonBlackLocator.CART_COUNTER], '2'))
        assert_manager.assert_contains(self.get_cart_counter(), '2')
        print('Narbut Carbon Black is added to cart')

