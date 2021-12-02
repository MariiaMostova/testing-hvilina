from enum import Enum
from website.locator.base_locator import BaseLocator


class FavouritePageLocator(BaseLocator, Enum):
    NARBUT_CARBON_BLACK_PRODUCT = '/html/body/div[1]/div[1]/section/div/div[2]/div/div/div'
