import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .pages.main_page import MainPage #импортируем класс описывающий главную страницу
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)                       # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                                          # открываем страницу
    page.go_to_login_page()                              # переходим на страницу логина. Этот метод описан в классе MainPage
    login_page = LoginPage(browser, browser.current_url) # создаем экземпляр класса LoginPage с его методами 
    login_page.should_be_login_page()                    # проверяем, что открылась страница логина (внутри этого метода три проверки)


def test_guest_should_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()