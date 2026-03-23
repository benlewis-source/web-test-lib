from __future__ import annotations


class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate_to(self, name: str) -> BasePage:
        from pages.cart import CartPage
        from pages.contact import ContactPage
        from pages.shop import ShopPage

        page_map = {
            "shop": ShopPage,
            "contact": ContactPage,
            "cart": CartPage,
        }
        if name not in page_map:
            raise ValueError(f"Unknown page: {name!r}")
        self.page.click(f"#nav-{name}")
        return page_map[name](self.page)
