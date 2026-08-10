from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        print("Url: ", self.browser.current_url)
        assert "basket" in self.browser.current_url, "'basket' doesn't find as a substring in a current URL page. Is it opened basket right now?"

    def should_be_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), "Basket not empty. Didn't find locator 'BASKET_IS_EMPTY_TEXT'"