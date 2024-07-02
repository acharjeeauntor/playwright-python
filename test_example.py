from playwright.sync_api import Page, expect
import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage

product_name = "Sauce Labs Onesie"
expect.set_options(timeout=10_000)

    
def testcase1(page: Page) -> None:
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    login_page.navigate("https://www.saucedemo.com/")
    login_page.login_to_app("standard_user","secret_sauce")
    page.wait_for_load_state('load')
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    product_page.add_to_cart_product(product_name)



def testcase2(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate("https://www.saucedemo.com/")
    login_page.login_to_app("standard_user","secret_sauce")
    page.wait_for_load_state('load')
    expect(page.locator("[data-test=\"title\"]")).to_be_visible()
    itemsLocator  = page.locator('[data-test="inventory-item-name"]').all()
    for item in range(len(itemsLocator)):
        if itemsLocator[item].text_content() == "Sauce Labs Onesie":
            itemsLocator[item].click()
            break