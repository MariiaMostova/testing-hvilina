from enum import Enum
from website.locator.base_locator import BaseLocator


class CartPageLocator(BaseLocator, Enum):
    FAVOURITE_PAGE_LINK = '/html/body/div[1]/div[1]/header/div[2]/div/div[6]/div[2]/a'
    CART_COUNTER = '/html/body/div[1]/div[1]/header/div[2]/div/div[6]/div[3]/div/a/span[2]/span'
    ADD_BUTTON = '//*[@id="cart_order_line_398719786"]/div[3]/div/div[2]'
    NARBUT_CARBON_BLACK_COUNT = '//*[@id="cart_order_line_398719786"]/div[3]/div/input//div'
    CREATE_ORDER_BUTTON = '//*[@id="cartform"]/div[2]/input'
