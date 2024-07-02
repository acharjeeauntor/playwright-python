class ProductPage:
    def __init__(self,page) -> None:
        self.page = page
        self.product_name = '[data-test="inventory-item-name"]'
        self.product_card = page.locator('[data-test="inventory-item-description"]')
        self.menu_button = page.locator('#react-burger-menu-btn')
        self.logout_button = page.locator('#logout_sidebar_link')
        self.cart_icon = page.locator('[data-test="shopping-cart-badge"]')
       


    def add_to_cart_product(self,name):
            itemsLocator  = self.product_card.all()
            for item in range(len(itemsLocator)):
                product_name = itemsLocator[item].locator(self.product_name).text_content()
                if  product_name == name:
                    itemsLocator[item].locator('button').click()
                    self.page.wait_for_timeout(5000)
                    break
    
    def logout_from_app(self):
         self.menu_button.click()
         self.logout_button.click()

    def get_cart_number(self):
         return self.cart_icon.text_content()
    
    def navigate_to_cart(self):
         self.cart_icon.click()
