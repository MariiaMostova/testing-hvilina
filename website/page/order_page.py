from selenium.webdriver.common.by import By

from website import assert_manager
from website.locator.order_page_locator import OrderPageLocator
from website.page.base import Base
from selenium.webdriver.support.expected_conditions import *


class OrderPage(Base):

    def check(self):
        order_summary = [By.XPATH, OrderPageLocator.CONFIRM_BUTTON]
        self.driver_wait.until(presence_of_element_located(order_summary))
        print('Order page opened')

    def validate_input(self, locator, text):
        elem = self.get_element_by_xpath(locator)
        elem.clear()
        elem.send_keys(text)
        self.driver_wait.until(text_to_be_present_in_element_value([By.XPATH, locator], text))
        assert_manager.assert_contains(elem.get_attribute('value'), text)

    def type_form(self):
        self.validate_input(OrderPageLocator.PHONE_NUMBER_INPUT, '0980980980')
        print('Phone number input validated')
        self.validate_input(OrderPageLocator.NAME_INPUT, "Марія К'юрі")
        print('Name input validated')
        self.validate_input(OrderPageLocator.EMAIL_INPUT, 'mary.kuri@gmail.com')
        print('Email input validated')

    def confirm(self):
        self.get_element_by_xpath(OrderPageLocator.CONFIRM_BUTTON).click()
        print('Confirm button clicked')
