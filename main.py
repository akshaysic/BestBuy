"""Provides a command-line interface for interacting with the store."""


from products import Product
from store import Store


def start(store):
    """Launch the interactive store menu for the user."""

    while True:
        print("\n   Store Menu\n   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ").strip()

        if choice == "1":
            for product in store.get_all_products():
                print(product.show())

        elif choice == "2":
            print(f"Total quantity in store: {store.get_total_quantity()}")

        elif choice == "3":
            order_list = []
            products_by_name = {p.name.lower(): p for p in store.get_all_products()}

            print("Enter products to order (leave product name empty to finish):")
            while True:
                name_input = input("Product name: ").strip().lower()
                if not name_input:
                    break

                product = products_by_name.get(name_input)
                if not product:
                    print("Product not found. Please try again.")
                    continue

                try:
                    qty_input = input(f"Quantity of '{product.name}': ").strip()
                    qty = int(qty_input)
                    if qty <= 0:
                        print("Please enter a positive quantity.")
                        continue

                    existing = next((item for item in order_list if item[0].name.lower() == name_input), None)
                    if existing:
                        index = order_list.index(existing)
                        order_list[index] = (existing[0], existing[1] + qty)
                    else:
                        order_list.append((product, qty))

                except ValueError:
                    print("Invalid quantity. Please enter a number.")

            if not order_list:
                print("No items ordered.")
            else:
                try:
                    total = store.order(order_list)
                    print(f"Order placed! Total cost: ${total:.2f}")
                except Exception as order_error:
                    print(f"Order failed: {order_error}")

        elif choice == "4":
            print("Thank you for visiting BestBuy!")
            break

        else:
            print("Invalid option. Please try again.")


def main():
    """Setup default inventory and start the store menu."""

    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
