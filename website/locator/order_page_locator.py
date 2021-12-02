from enum import Enum
from website.locator.base_locator import BaseLocator


class OrderPageLocator(BaseLocator, Enum):
    PHONE_NUMBER_INPUT = '//*[@id="client_phone"]'
    NAME_INPUT = '//*[@id="client_name"]'
    EMAIL_INPUT = '//*[@id="client_email"]'
    CONFIRM_BUTTON = '//*[@id="create_order"]'
    ORDER_SUMMARY = '/html/body/section/div/div/div[2]/div/div]'
