from playwright.sync_api import expect

from pages.base import BasePage


class Product:
    def __init__(self, element):
        self.element = element
        self.title = self.element.locator(".product-title").inner_text()
        self.price = float(self.element.locator(".product-price").inner_text().strip("$"))

    def buy(self):
        self.element.locator("a", has_text="Buy").click()


class ShopPage(BasePage):
    def __init__(self, page):
        super().__init__(page=page)
        self.products = {}
        # Product elements are not available instantaneously
        self.page.wait_for_selector("[id^='product-']")
        for element in self.page.locator("[id^='product-']").all():
            product = Product(element)
            self.products[product.title] = product

    def buy(self, title: str, count: int = 1):
        try:
            product: Product = self.products[title]
        except KeyError:
            raise KeyError(f"Product '{title}' is not a valid product title")

        if count < 1:
            raise ValueError("Count cannot be less than 1")

        target_count = int(self.page.locator(".cart-count").inner_text()) + count
        for _ in range(count):
            product.buy()
        # Ensures the cart page is accurate immediately after this function returns 
        expect(self.page.locator(".cart-count")).to_have_text(str(target_count))
