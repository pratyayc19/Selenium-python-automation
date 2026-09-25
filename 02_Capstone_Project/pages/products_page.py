from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductsPage(BasePage):

    PRODUCTS_LINK = (
        By.XPATH,
        "//a[contains(@href,'/products')]"
    )

    SEARCH_INPUT = (By.ID, "search_product")

    SEARCH_BUTTON = (By.ID, "submit_search")

    SEARCH_RESULTS_TITLE = (
        By.XPATH,
        "//h2[contains(text(),'Searched Products')]"
    )

    SEARCHED_PRODUCTS = (
        By.XPATH,
        "//div[contains(@class,'productinfo')]//p"
    )

    def open_products_page(self):
        self.safe_click(self.PRODUCTS_LINK)

    def search_product(self, product_name):
        self.safe_type(self.SEARCH_INPUT, product_name)
        self.safe_click(self.SEARCH_BUTTON)

    def is_search_results_displayed(self):
        return self.is_visible(self.SEARCH_RESULTS_TITLE)

    def is_product_displayed(self, product_name):
        products = self.driver.find_elements(
            *self.SEARCHED_PRODUCTS
        )

        return any(
            product_name.lower() in product.text.lower()
            for product in products
        )