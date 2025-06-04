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
            products = store.get_all_products()

            while True:
                print("\nAvailable Products:")
                for i, p in enumerate(products, 1):
                    print(f"{i}. {p.name} (In stock: {p.quantity})")

                selection = input("Enter the product number to order (leave blank to finish): ").strip()
                if not selection:
                    break

                try:
                    index = int(selection) - 1
                    if 0 <= index < len(products):
                        product = products[index]
                        qty_input = input(f"Enter quantity for '{product.name}': ").strip()
                        qty = int(qty_input)

                        if qty <= 0:
                            print("Please enter a positive quantity.")
                            continue

                        existing = next((item for item in order_list if item[0] == product), None)
                        if existing:
                            order_list = [(p, q + qty) if p == product else (p, q) for p, q in order_list]
                        else:
                            order_list.append((product, qty))

                        print(f"✅ Added {qty} of '{product.name}' to your order.")
                    else:
                        print("Invalid product number. Try again.")
                except ValueError:
                    print("Please enter a valid number.")

            if not order_list:
                print("No items ordered.")
            else:
                try:
                    total = store.order(order_list)
                    print(f"\n🎉 Order placed! Total cost: ${total:.2f}")
                except Exception as order_error:
                    print(f"❌ Order failed: {order_error}")

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
