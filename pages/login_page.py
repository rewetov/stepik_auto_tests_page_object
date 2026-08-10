from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        print("Текущий URL: ", self.browser.current_url)
        assert "login" in self.browser.current_url, "'login' doesn't find as a substring a test URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        user_email = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL_INPUT).send_keys(email)
        user_password = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_INPUT).send_keys(password)
        user_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_CONFIRM_INPUT).send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()