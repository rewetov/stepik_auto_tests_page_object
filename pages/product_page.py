from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def add_product_to_basket(self):
		add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
		add_to_basket_button.click() 

	def should_be_product_page(self):
		assert self.is_element_present(*ProductPageLocators.DESCRIPTION), "Description not presented, looks like product page not opened"

	def book_name_in_message_is_the_same_as_on_the_page(self):
		bookname_message = self.is_element_text(*ProductPageLocators.PRODUCT_WAS_ADDED_TO_BASKET_MESSAGE)
		bookname = self.is_element_text(*ProductPageLocators.PRODUCT_NAME)
		print("bookname_message =", bookname_message)
		print("bookname =", bookname)
		assert bookname_message == bookname, "Book name in the sucess message not equal the name of product on the page"


	def price_in_the_basket_message_the_same_as_book_price(self):
		book_price_message = self.is_element_text(*ProductPageLocators.PRODUCT_PRICE_BASKET_MESSAGE)
		book_price = self.is_element_text(*ProductPageLocators.PRODUCT_PRICE)
		print("book_price_message =", book_price_message)
		print("book_price =", book_price)
		assert book_price_message == book_price, "Book price in the sucess basket message not equal the price of product on the page"