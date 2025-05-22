from conftest import profile_page


def test_field_block(profile_page):
    profile_page.log_in()
    profile_page.click_add_inventory_button()
    profile_page.is_cart_item_quantity_one()