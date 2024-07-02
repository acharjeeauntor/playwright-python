class LoginPage:
    def __init__(self,page) -> None:
        self.page = page
        self.email_input =  page.locator("[data-test=\"username\"]")
        self.pass_input =  page.locator("[data-test=\"password\"]")
        self.login_button =   page.locator("[data-test=\"login-button\"]")

    def navigate(self,url):
        self.page.goto(url)
        
    def login_to_app(self,email,password):
       self.email_input.fill(email)
       self.pass_input.fill(password)
       self.login_button.click()