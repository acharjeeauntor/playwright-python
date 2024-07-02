from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import json

with open('data.json') as f:
    data = json.load(f)

product_name = "Sauce Labs Onesie"
expect.set_options(timeout=10_000)

# def test1_login_logout_test(page: Page) -> None:
#     login_page = LoginPage(page)
#     product_page = ProductPage(page)
#     login_page.navigate("https://www.saucedemo.com/")
#     login_page.login_to_app("standard_user","secret_sauce")
#     page.wait_for_load_state('load')
#     product_page.logout_from_app()
#     expect(page.locator("[data-test=\"title\"]")).not_to_be_visible()
    
# def test2_add_to_cart_product_test(page: Page) -> None:
#     login_page = LoginPage(page)
#     product_page = ProductPage(page)
#     login_page.navigate("https://www.saucedemo.com/")
#     login_page.login_to_app("standard_user","secret_sauce")
#     page.wait_for_load_state('load')
#     expect(page.locator("[data-test=\"title\"]")).to_be_visible()
#     product_page.add_to_cart_product(product_name)
#     expect(product_page.cart_icon).to_have_text("1")

'''
    itemsLocator  = page.locator('[data-test="inventory-item-name"]').all()
    for item in range(len(itemsLocator)):
        if itemsLocator[item].text_content() == "Sauce Labs Onesie":
            itemsLocator[item].click()
            break
'''
def test3_order_product_e2e_test(page: Page) -> None:
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)


    login_page.navigate("https://www.saucedemo.com/")
    login_page.login_to_app("standard_user","secret_sauce")
    page.wait_for_load_state('load')
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    product_page.add_to_cart_product(data.product_name)
    expect(product_page.cart_icon).to_have_text("1")
    product_page.navigate_to_cart()
    expect(cart_page.product_name).to_have_text(product_name)
    expect(cart_page.remove_button).to_be_visible()
    cart_page.click_checkout()

    checkout_page.enter_info("Auntor","Acharja","1912")
    expect(checkout_page.product_name).to_have_text(product_name)
    checkout_page.finish_checkout()

    expect(checkout_page.confirmation_msg).to_have_text("Thank you for your order!")
    expect(checkout_page.title_status).to_contain_text("Complete!")



