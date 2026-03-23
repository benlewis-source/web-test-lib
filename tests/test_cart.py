from pages.cart import CartPage
from pages.home import HomePage
from pages.shop import ShopPage


def test_cart(jupiter_toys: HomePage):
    purchases = {"Stuffed Frog": 2, "Fluffy Bunny": 5, "Valentine Bear": 3}

    shop: ShopPage = jupiter_toys.navigate_to("shop")
    for title, count in purchases.items():
        shop.buy(title, count)

    prices = {title: shop.products[title].price for title in purchases}

    cart: CartPage = shop.navigate_to("cart")
    running_total = 0
    for title, count in purchases.items():
        running_total += prices[title] * count
        assert cart.get_price(title) == prices[title]
        assert cart.get_subtotal(title) == prices[title] * count

    assert cart.get_total() == running_total
