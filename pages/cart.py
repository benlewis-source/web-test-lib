import pandas as pd

from pages.base import BasePage


class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.table: pd.DataFrame = self._load_table()

    def _load_table(self) -> pd.DataFrame:
        rows = []
        self.page.wait_for_selector("tr.cart-item")
        for row in self.page.locator("tr.cart-item").all():
            cells = row.locator("td")
            item = cells.nth(0).inner_text().strip()
            price = float(cells.nth(1).inner_text().strip().lstrip("$"))
            quantity = int(cells.nth(2).locator("input").get_attribute("value"))
            subtotal = float(cells.nth(3).inner_text().strip().lstrip("$"))
            rows.append({"item": item, "price": price, "quantity": quantity, "subtotal": subtotal})
        return pd.DataFrame(rows).set_index("item")

    def get_price(self, title: str) -> float:
        return float(self.table.loc[title].price)

    def get_subtotal(self, title: str) -> float:
        return float(self.table.loc[title].subtotal)

    def get_total(self) -> float:
        return float(self.table.subtotal.sum())
