from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import json
import os


# Extract json Data
data_file_path = os.path.join('test_data', 'data.json')
with open(data_file_path) as f:
    data = json.load(f)

# Store the test data
product_name = data['product_name']
username = data['username']
password = data['password']
confirmation_msg = data['order_confirmation_msg']
confirmation_status = data['order_complete_status']
expect.set_options(timeout=10_000)


# Test cases Started from here

def test1_login_logout_test(page: Page) -> None:
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    
    login_page.navigateToApp()
    login_page.login_to_app(username,password)
    page.wait_for_load_state('load')
    product_page.logout_from_app()
    expect(page.locator("[data-test=\"title\"]")).not_to_be_visible()
    
def test2_add_to_cart_product_test(page: Page) -> None:
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.navigateToApp()
    login_page.login_to_app(username,password)
    page.wait_for_load_state('load')
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    product_page.add_to_cart_product(product_name)
    expect(product_page.cart_icon).to_have_text("1")

'''
    itemsLocator  = page.locator('[data-test="inventory-item-name"]').all()
    for item in range(len(itemsLocator)):
        if itemsLocator[item].text_content() == "Sauce Labs Onesie":
            itemsLocator[item].click()
            break
'''
