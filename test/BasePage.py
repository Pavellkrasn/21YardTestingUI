class BasePage:
    def __init__(self, page):
        self.page = page

    def open (self):
        self.page.goto("https://dev.21yard.com/")




