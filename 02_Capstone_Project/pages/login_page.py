from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_LINK = (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGGED_IN_USER = (By.XPATH, "//a[contains(text(),'Logged in as')]")

    def open_login_page(self):
        self.safe_click(self.LOGIN_LINK)

    def login(self, email, password):
        self.safe_type(self.EMAIL_INPUT, email)
        self.safe_type(self.PASSWORD_INPUT, password)
        self.safe_click(self.LOGIN_BUTTON)

    def is_logged_in(self):
        return self.is_visible(self.LOGGED_IN_USER)