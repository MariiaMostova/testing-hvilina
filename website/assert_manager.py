from selenium.webdriver.remote.webelement import WebElement


def assert_contains(text, substr):
    assert substr in text


def assert_changed(old, new):
    assert old != new


def assert_visibility(elem: WebElement):
    assert elem.is_displayed()
