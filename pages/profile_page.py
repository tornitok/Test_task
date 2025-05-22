from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from support.assertions import Assertions


class InventoryPage(LoginPage):
    ADD_INVENTORY_BUTTON = (By.CSS_SELECTOR, '.inventory_item:nth-of-type(1) button')
    SHOPPING_CART_BUTTON = (By.CSS_SELECTOR, '.shopping_cart_link')
    CART_BADGE = (By.CSS_SELECTOR, '.shopping_cart_badge')

    def __init__(self, driver):
        super().__init__(driver)
        self.assertion = Assertions

    def log_in(self):
        self.enter_email()
        self.enter_password()
        self.click_button()

    def click_add_inventory_button(self):
        self.click(self.ADD_INVENTORY_BUTTON)

    def is_cart_item_quantity_one(self):
        cart_count = self.get_text(self.CART_BADGE)

        self.assertion.assert_equal(
            expected="1",
            actual=cart_count
        )