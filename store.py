from products import Product

class Store:
    def __init__(self, products=None):
        if products is None:
            self.products = []
        else:
            self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        total = 0
        for product, quantity in shopping_list:
            total += product.buy(quantity)
        return total


if __name__ == "__main__":
    from products import Product

    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()

    print(best_buy.get_total_quantity())  # should print total quantity
    print(best_buy.order([(products[0], 1), (products[1], 2)]))  # should print total cost of this order
