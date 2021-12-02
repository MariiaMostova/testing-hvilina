from enum import Enum
from website.locator.base_locator import BaseLocator


class MainPageLocator(BaseLocator, Enum):
    HEADER_MENU_ITEM_CATALOG = '/html/body/div[1]/div[1]/header/div[2]/div/div[2]/div/ul/li[1]'
    CATALOG_ITEM_FOR_HER = '/html/body/div[1]/div[1]/header/div[2]/div/div[2]/div/ul/li[1]/ul/li[1]/a'
    CATALOG_ITEM_FOR_HIM = '/html/body/div[1]/div[1]/header/div[2]/div/div[2]/div/ul/li[1]/ul/li[2]/a'
    SLIDER = '/html/body/div[1]/div[1]/section/section/div'
