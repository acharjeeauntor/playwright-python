class CheckoutPage:
    def __init__(self,page) -> None:
        self.page = page
        self.first_name = page.locator('#first-name')
        self.last_name = page.locator('#last-name')
        self.postal_code = page.locator('#postal-code')
        self.continue_button = page.locator('#continue')
        self.product_name = page.locator('[data-test="inventory-item-name"]')
        self.finish_button = page.locator('#finish')
        self.confirmation_msg = page.locator('[data-test="complete-header"]')
        self.title_status = page.locator('[data-test="title"]')
       
       
    def enter_info(self,fname,lname,postal_code):
        self.first_name.fill(fname)
        self.last_name.fill(lname)
        self.postal_code.fill(postal_code)
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()