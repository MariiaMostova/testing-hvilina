from enum import Enum
from website.locator.base_locator import BaseLocator


class NarbutSilverGreyLocator(BaseLocator, Enum):
    ADD_TO_CART_BUTTON = '//*[@id="add__to_cart"]'
    CART_COUNTER = '/html/body/div[1]/div[1]/header/div[2]/div/div[6]/div[3]/div/a/span[2]/span'
