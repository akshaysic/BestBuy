"""Defines the Store class for managing product operations in the store."""

from products import Product

class Store:
    """Represents a store that manages multiple products."""

    def __init__(self, products=None):
        """Initialize the store with an optional list of products."""
        if products is None:
            self.products = []
        else:
            self.products = products

    def add_product(self, product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store if it exists."""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """Return the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        """Return a list of all active products in the store."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """Process an order list and return the total cost."""
        total = 0
        for product, quantity in shopping_list:
            cost = product.buy(quantity)
            print(f"{product.name}: requested {quantity}, purchased for ${cost:.2f}")
            total += cost
        return total


if __name__ == "__main__":
    # Setup products and test store functionality
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    active_products = best_buy.get_all_products()

    print(f"Total quantity in store: {best_buy.get_total_quantity()}")
    total_cost = best_buy.order([
        (active_products[0], 1),
        (active_products[1], 2)
    ])
    print(f"Total cost of order: ${total_cost:.2f}")
