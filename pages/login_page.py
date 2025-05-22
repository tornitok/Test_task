from selenium.webdriver.common.by import By

from base.base_object import BaseObject
from config import Secrets
from support.assertions import Assertions


class LoginPage(BaseObject):
    USER_NAME_FIELD = (By.CSS_SELECTOR, '#user-name')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button')
    INVENTORY_ITEMS = (By.CSS_SELECTOR, "#inventory_container .inventory_item")

    def __init__(self, driver):
        super().__init__(driver)
        self.assertion = Assertions

    def enter_email(self, user_name=Secrets.USER_NAME):
        self.send_keys(self.USER_NAME_FIELD, user_name)

    def enter_password(self, password=Secrets.PASSWORD):
        self.send_keys(self.PASSWORD_FIELD, password)

    def click_button(self):
        self.click(self.LOGIN_BUTTON)


    def count_inventory_items(self, expected_count=6):
        self._is_present(self.INVENTORY_ITEMS)
        items = self.find_elements(self.INVENTORY_ITEMS)
        actual_count = len(items)
        self.assertion.assert_equal(
            actual=actual_count,
            expected=expected_count,
        )
