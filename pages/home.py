from pages.base import BasePage


class HomePage(BasePage):
    def __init__(self, page, base_url: str):
        super().__init__(page=page)
        self.base_url = base_url
        self.page.goto(base_url)
