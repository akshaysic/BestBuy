from products import Product
from store import Store

def start(store):
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
            print("Enter the quantity for each product:")
            order_list = []
            for product in store.get_all_products():
                print(product.show())
                try:
                    qty_input = input(f"Quantity of '{product.name}': ").strip()
                    if qty_input == "":
                        continue
                    qty = int(qty_input)
                    if qty > 0:
                        order_list.append((product, qty))
                except ValueError:
                    print("Invalid input, skipping...")
            try:
                total = store.order(order_list)
                print(f"Order placed! Total cost: ${total}")
            except Exception as e:
                print(f"Order failed: {e}")
        elif choice == "4":
            print("Thank you for visiting BestBuy!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = Store(product_list)
    start(best_buy)
