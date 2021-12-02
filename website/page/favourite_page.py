from website.locator.favourite_page_locator import FavouritePageLocator
from website.page.base import Base
from website.page.narbut_carbon_black_page import NarbutCarbonBlackPage


class FavouritePage(Base):

    def check(self):
        super().check()
        print('Favourite page opened')

    def open_narbut_carbon_black_page(self):
        product = FavouritePageLocator.NARBUT_CARBON_BLACK_PRODUCT
        self.click(product)

