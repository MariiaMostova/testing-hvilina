from enum import Enum
from website.locator.base_locator import BaseLocator


class ForHerPageLocator(BaseLocator, Enum):

    COLLECTIONS = '//*[@id="characteristics"]/div[1]'
    COLLECTIONS_OPTIONS = '//*[@id="characteristics"]/div[1]/ul'
    NARBUT_COLLECTIONS_FILTER_ITEM = '//*[@id="characteristics"]/div[1]/ul/li[2]'
    SELECTED_INDICATOR = '/html/body/div[1]/div[1]/section/div/div/div[1]/div/div[1]/div[2]/form/div[1]/label/span[1]'
    NARBUT_CHECKBOX = '//*[@id="characteristics"]/div[1]/ul/li[2]/input[1]'
    FAVOURITE_BUTTON = '/html/body/div[1]/div[1]/section/div/div/div[2]/div[2]/div[1]/div/button'
    ADDED_TO_FAVOURITE_INDICATOR = '/html/body/div[1]/div[1]/section/div/div/div[2]/div[2]/div[1]/div/button/img[2]'
    FAVOURITE_COUNTER = '/html/body/div[1]/div[1]/header/div[2]/div/div[6]/div[2]/a/span[2]/span'
    NARBUT_SILVER_GREY_BLACK_PRODUCT = '/html/body/div[1]/div[1]/section/div/div/div[2]/div[2]/div[9]/div'