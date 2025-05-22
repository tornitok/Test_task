import pytest

from conftest import login_page


def test_success_log_in(login_page):
    login_page.enter_email()
    login_page.enter_password()
    login_page.click_button()
    login_page.count_inventory_items()