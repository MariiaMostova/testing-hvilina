from selenium import webdriver


class DriverFactory:
    __web_driver = None

    @classmethod
    def get_driver(cls, name='chrome'):
        if not cls.__web_driver:
            if name == 'chrome':
                _driver = webdriver.Chrome()
                print('Driver is Chrome')
            elif name == 'opera':
                _driver = webdriver.Opera()
                print('Driver is Opera')
            elif name == 'firefox':
                _driver = webdriver.Firefox()
                print('Driver is Firefox')
            elif name == 'edge':
                _driver = webdriver.Edge()
                print('Driver is Edge')
            elif name == 'safari':
                _driver = webdriver.Safari()
                print('Driver is Safari')
            else:
                raise ValueError('Unknown browser')
            cls.__web_driver = _driver
        return cls.__web_driver
