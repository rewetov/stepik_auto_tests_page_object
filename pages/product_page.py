from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def add_product_to_basket(self):
		add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
		add_to_basket_button.click() 

	def should_be_product_page(self):
		assert self.is_element_present(*ProductPageLocators.DESCRIPTION), "Description not presented, looks like product page not opened"
	
	#проверяем, что название книги в сообщении об успешном добавлении книги в корзину действительно соответствует ее названию
	def book_name_in_message_is_the_same_as_on_the_page(self):
		bookname_message = self.is_element_text(*ProductPageLocators.PRODUCT_WAS_ADDED_TO_BASKET_MESSAGE)
		bookname = self.is_element_text(*ProductPageLocators.PRODUCT_NAME)
		print("bookname_message =", bookname_message)
		print("bookname =", bookname)
		assert bookname_message == bookname, "Book name in the sucess message not equal the name of product on the page"

	#проверяем, что цена в сообщении об успешном добавлении книги в корзину соответствует стоимости самой книги
	def price_in_the_basket_message_the_same_as_book_price(self):
		book_price_message = self.is_element_text(*ProductPageLocators.PRODUCT_PRICE_BASKET_MESSAGE)
		book_price = self.is_element_text(*ProductPageLocators.PRODUCT_PRICE)
		print("book_price_message =", book_price_message)
		print("book_price =", book_price)
		assert book_price_message == book_price, "Book price in the sucess basket message not equal the price of product on the page"

	#Проверяем, что нет сообщения об успехе с помощью is_not_element_present. Метод is_not_element_present возвращает True если элемент не найден и False если найден.
	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

	#Проверяем, что нет сообщения об успехе с помощью is_disappeared
	def should_disappear_success_message(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message didin't disappear from product page"