from selenium.webdriver.remote.webdriver import WebDriver

from driver.driver_factory import DriverFactory


class DriverConnection:
    __driver = None

    def __init__(self, browser_name, url):
        if not DriverConnection.__driver:
            DriverConnection.__driver = DriverFactory.get_driver(browser_name)
            DriverConnection.__driver.implicitly_wait(10)
            DriverConnection.__driver.get(url)
            DriverConnection.__driver.set_window_size(1920, 1080)
            print('New driver connection is opened')
        else:
            print(self.get_connection(browser_name, url), ' is connected')

    @classmethod
    def get_connection(cls, browser_name, url) -> WebDriver:
        if not cls.__driver:
            cls.__driver = DriverConnection(browser_name, url).__driver
        return cls.__driver


DriverConnection.get_connection('chrome', 'https://hvilina.com.ua/')
