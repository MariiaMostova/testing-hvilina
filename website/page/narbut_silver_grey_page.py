from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element, visibility_of_element_located
from website.locator.narbut_silver_grey_locator import NarbutSilverGreyLocator
from website.page.base import Base


class NarbutSilverGreyPage(Base):

    def check(self):
        super().check()
        print('Narbut Silver Grey page opened')

    def get_cart_counter(self):
        cart_counter = self.get_element_by_xpath(NarbutSilverGreyLocator.CART_COUNTER).text
        print('Cart counter:', cart_counter)

    def add_to_cart(self):
        self.get_cart_counter()
        self.get_element_by_xpath(NarbutSilverGreyLocator.ADD_TO_CART_BUTTON).click()
        assert self.driver_wait.until(
            text_to_be_present_in_element([By.XPATH, NarbutSilverGreyLocator.CART_COUNTER], '1'))
        self.get_cart_counter()
        print('Narbut Silver Grey is added to cart')
