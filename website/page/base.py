from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait
from website.locator.base_locator import BaseLocator


class Base:
    driver = None
    driver_wait = None
    action_chain = None

    def __init__(self, driver):
        self.driver = driver
        self.driver_wait = WebDriverWait(self.driver, 10)
        self.action_chain = ActionChains(self.driver)

    def check(self):
        header = [By.XPATH, BaseLocator.HEADER]
        self.driver_wait.until(presence_of_element_located(header))

    def get_element_by_xpath(self, locator) -> WebElement:
        return self.driver.find_element_by_xpath(locator)

    def click(self, locator):
        elem = self.get_element_by_xpath(locator)
        self.action_chain.click(elem).perform()

    def hover(self, locator):
        elem = self.get_element_by_xpath(locator)
        self.action_chain.move_to_element(elem).perform()

