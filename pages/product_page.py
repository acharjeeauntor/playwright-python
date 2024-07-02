class ProductPage:
    def __init__(self,page) -> None:
        self.page = page
        self.product_name = '[data-test="inventory-item-name"]'
        self.product_card = page.locator('[data-test="inventory-item-description"]')


    def add_to_cart_product(self,name):
            itemsLocator  = self.product_card.all()
            for item in range(len(itemsLocator)):
                product_name = itemsLocator[item].locator(self.product_name).text_content()
                if  product_name == name:
                    itemsLocator[item].locator('button').click()
                    self.page.wait_for_timeout(5000)
                    break
