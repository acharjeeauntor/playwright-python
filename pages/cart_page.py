class CartPage:
    def __init__(self,page) -> None:
        self.page = page
        self.product_name = page.locator('[data-test="inventory-item-name"]')
        self.remove_button = page.locator('.cart_button')
        self.checkout_button = page.locator('#checkout')
       
    def click_checkout(self):
        self.checkout_button.click()