"""Defines the Product class for managing store inventory."""

class Product:
    """Represents a product with name, price, quantity, and active status."""

    def __init__(self, name, price, quantity):
        """Initialize the product with a name, price, and quantity."""
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid product data")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """Return the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Update the product quantity and deactivate if quantity is zero."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """Return True if the product is active, False otherwise."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Return a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """Buy the given quantity if available; return the total price."""
        if not self.active:
            raise Exception("Product is not active")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if self.quantity == 0:
            raise Exception("Product is out of stock")

        actual_quantity = min(quantity, self.quantity)
        self.quantity -= actual_quantity
        if self.quantity == 0:
            self.deactivate()

        if actual_quantity < quantity:
            print(f"Note: Only {actual_quantity} units were available and purchased.")
        return actual_quantity * self.price
