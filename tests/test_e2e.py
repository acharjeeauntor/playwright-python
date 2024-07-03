from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import json
import os
from faker import Faker


# Extract json Data
data_file_path = os.path.join('test_data', 'data.json')
with open(data_file_path) as f:
    data = json.load(f)

# Initialization of Faker
faker  = Faker()

# Store the test data
product_name = data['product_name']
username = data['username']
password = data['password']
confirmation_msg = data['order_confirmation_msg']
confirmation_status = data['order_complete_status']
first_name = faker.first_name()
last_name = faker.last_name()
postcode = faker.postcode()


expect.set_options(timeout=10_000)


# Test cases Started from here

def test3_order_product_e2e_test(page: Page) -> None:
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)


    login_page.navigateToApp()
    login_page.login_to_app(username,password)
    page.wait_for_load_state('load')
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    product_page.add_to_cart_product(product_name)
    expect(product_page.cart_icon).to_have_text("1")
    product_page.navigate_to_cart()
    expect(cart_page.product_name).to_have_text(product_name)
    expect(cart_page.remove_button).to_be_visible()
    cart_page.click_checkout()

    checkout_page.enter_info(first_name,last_name,postcode)
    expect(checkout_page.product_name).to_have_text(product_name)
    checkout_page.finish_checkout()

    expect(checkout_page.confirmation_msg).to_have_text(confirmation_msg)
    expect(checkout_page.title_status).to_contain_text(confirmation_status)



