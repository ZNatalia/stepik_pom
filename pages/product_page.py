import time
from .base_page import BasePage
from .locators import ProductPageLocators, MainPageLocators


class ProductPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*ProductPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_product_page(self):
        self.should_be_button_add_to_basket()
        self.should_be_price()
        self.should_be_stock_shown()



    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "The 'Add to basket' button is not present"


    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE), "The price is not present"


    def should_be_stock_shown(self):
        assert self.is_element_present(*ProductPageLocators.STOCK_AVAILABILITY), "The 'Stock availability' button is not present"

    def guest_can_add_item_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()
        name_of_book_in_prod_page = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK).text
        name_of_book_in_alert = self.browser.find_element(*ProductPageLocators.INNERALERT_ITEM_ADDDED).text
        price_in_alert = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE).text
        book_price_on_page = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        assert name_of_book_in_prod_page in name_of_book_in_alert
        assert "has been added" in name_of_book_in_alert
        assert book_price_on_page in price_in_alert
        self.should_be_view_basket_link()
        self.should_be_checkout_now_link()
        # time.sleep(50)

    def should_be_view_basket_link(self):
        assert "View basket" == self.browser.find_element(*ProductPageLocators.VIEW_BASKET_LINK).text

    def should_be_checkout_now_link(self):
        assert "View basket" == self.browser.find_element(*ProductPageLocators.VIEW_BASKET_LINK).text


