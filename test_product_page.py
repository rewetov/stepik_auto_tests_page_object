import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)                       # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                                             # открываем страницу
    page.add_product_to_basket()                            # добавляем продукт в корзину
    page.solve_quiz_and_get_code()
    page.book_name_in_message_is_the_same_as_on_the_page()
    page.price_in_the_basket_message_the_same_as_book_price()
