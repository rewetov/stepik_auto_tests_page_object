import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import time

urls = [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{no}" for no in range(1)]


#@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)                       # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                                             # открываем страницу
    page.add_product_to_basket()                            # добавляем продукт в корзину
    page.solve_quiz_and_get_code()
    page.book_name_in_message_is_the_same_as_on_the_page()
    page.price_in_the_basket_message_the_same_as_book_price()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()  
    page.should_not_be_success_message()
    
    #Открываем страницу товара 
    #Добавляем товар в корзину 
    #Проверяем, что нет сообщения об успехе с помощью is_not_element_present

def test_guest_cant_see_success_message(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()  
    page.should_disappear_success_message()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)                       # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                                          # открываем страницу
    page.go_to_login_page()                              # переходим на страницу логина. Этот метод описан в классе MainPage
    login_page = LoginPage(browser, browser.current_url) # создаем экземпляр класса LoginPage с его методами 
    login_page.should_be_login_page()                    # проверяем, что открылась страница логина (внутри этого метода три проверки)

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_basket_page()
    basket.should_be_basket_is_empty()
    time.sleep(3)