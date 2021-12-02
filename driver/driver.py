from driver.driver_factory import DriverFactory


class Driver:

    @staticmethod
    def get(name):
        DriverFactory.get_driver(name)
