from driver.connection import DriverConnection
from pytest import fixture
from website.page.cart_page import CartPage
from website.page.favourite_page import FavouritePage
from website.page.for_her_page import ForHerPage
from website.page.main_page import MainPage
from website.page.narbut_carbon_black_page import NarbutCarbonBlackPage
from website.page.narbut_silver_grey_page import NarbutSilverGreyPage
from website.page.order_page import OrderPage


class TestHvilinaNarbutOrder:
    @fixture
    def driver(self):
        return DriverConnection.get_connection('chrome', 'https://hvilina.com.ua')

    def test_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.check()
        main_page.catalog_menu_item_hover()
        main_page.for_her_catalog_item_click()

    def test_for_her_page(self, driver):
        for_her_page = ForHerPage(driver)
        for_her_page.check()
        for_her_page.open_collections_filter_options()
        for_her_page.filter_by_narbut_collection()
        for_her_page.check_narbut_collection_checkbox()
        for_her_page.add_narbut_carbon_black_to_favourite()
        for_her_page.open_narbut_silver_grey_page()

    def test_add_to_cart_from_main_page(self, driver):
        narbut_silver_grey_page = NarbutSilverGreyPage(driver)
        narbut_silver_grey_page.check()
        narbut_silver_grey_page.add_to_cart()

        cart_page = CartPage(driver)
        cart_page.check()
        cart_page.open_favourite_page()

    def test_add_to_cart_from_favourite_page(self, driver):
        favourite_page = FavouritePage(driver)
        favourite_page.check()
        favourite_page.open_narbut_carbon_black_page()

        narbut_carbon_black_page = NarbutCarbonBlackPage(driver)
        narbut_carbon_black_page.check()
        narbut_carbon_black_page.add_to_cart()

        cart_page = CartPage(driver)
        cart_page.add_number_for_narbut_carbon_black()
        cart_page.create_order()

    def test_create_order(self, driver):
        order_page = OrderPage(driver)
        order_page.check()
        order_page.type_form()
        order_page.confirm()

        driver.quit()
