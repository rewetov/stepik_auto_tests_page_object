from selenium.webdriver.common.by import By


class LoginPageLocators():
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
	ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button")
	DESCRIPTION = (By.CSS_SELECTOR, "#product_description")
	PRODUCT_WAS_ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
	PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
	PRODUCT_PRICE_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert-info.fade.in > div > p:nth-child(1) > strong")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info.fade.in > div > p:nth-child(1) > strong")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")