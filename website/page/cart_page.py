from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from website.locator.cart_page_locator import CartPageLocator
from website.page.base import Base
import website.assert_manager as assert_manager

class CartPage(Base):

    def check(self):
        super().check()
        print('Cart page opened')

    def open_favourite_page(self):
        old_url = self.driver.current_url
        self.click(CartPageLocator.FAVOURITE_PAGE_LINK)
        new_url = self.driver.current_url
        assert_manager.assert_changed(old_url, new_url)

    def add_number_for_narbut_carbon_black(self):
        self.get_element_by_xpath(CartPageLocator.ADD_BUTTON).click()
        self.driver_wait.until(text_to_be_present_in_element([By.XPATH, CartPageLocator.CART_COUNTER], '2'))
        elem = self.get_element_by_xpath(CartPageLocator.CART_COUNTER)
        assert_manager.assert_contains(elem.text, '2')
        print('Add number button clicked')

    def get_product_counter(self):
        cart_counter = self.get_element_by_xpath(CartPageLocator.CART_COUNTER).text
        print('Narbut Carbon Black counter:', cart_counter)

    def create_order(self):
        old_url = self.driver.current_url
        button = self.get_element_by_xpath(CartPageLocator.CREATE_ORDER_BUTTON)
        button.click()
        new_url = self.driver.current_url
        assert_manager.assert_changed(old_url, new_url)
        print('Order created')
