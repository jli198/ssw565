
class Order:
    def __init__(self, order_id, customers):
        """
        Initialize the order with an ID and a list of customers.
        :param order_id: Unique identifier for the order.
        :param customers: List of dictionaries containing customer info (name and contact).
        """
        self.order_id = order_id
        self.status = "Order Placed"
        self.customers = customers  # List of customer dictionaries

    def update_status(self, status):
        """
        Update the status of the order and notify all customers.
        :param status: New status for the order (e.g., "Preparing", "Out for Delivery").
        """
        self.status = status
        print(f"Order {self.order_id}: Status updated to '{self.status}'")
        self.notify_customers()

    def notify_customers(self):
        """
        Notify all customers about the status update.
        """
        for customer in self.customers:
            name = customer['name']
            contact = customer['contact']
            print(f"Notifying {name} at {contact}: Order {self.order_id} is now '{self.status}'")
# Client Code
def main():
    # List of customers for the order
    customers = [
        {"name": "Alice", "contact": "alice@example.com"},
        {"name": "Bob", "contact": "bob@example.com"}
    ]

    # Create an order with customers
    order = Order(order_id=101, customers=customers)

    # Update the order status and notify customers
    order.update_status("Preparing")
    order.update_status("Out for Delivery")
    order.update_status("Delivered")


if __name__ == "__main__":
    main()






########


1. Subject (Observable)

The Order class acts as the observable. It maintains a list of observers (subscribers) and notifies them of changes.


class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.status = "Order Placed"
        self.observers = []  # List of subscribers

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.order_id, self.status)

    def update_status(self, status):
        self.status = status
        print(f"Order {self.order_id}: Status updated to '{self.status}'")
        self.notify_observers()


2. Observer Interface

Define an interface for observers to implement the update method.



class Observer:
    def update(self, order_id, status):
        raise NotImplementedError("Subclasses must implement this method.")


3. Concrete Observers

Implement specific observers, such as customers, who will receive notifications.



class Customer(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, order_id, status):
        print(f"Notification for {self.name}: Order {order_id} is now '{status}'")



4. Client Code

Simulate the pizza ordering process with an order and customer notifications.


def main():
    # Create an order
    order = Order(order_id=101)
    
    # Create customers (observers)
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    
    # Subscribe customers to the order
    order.add_observer(customer1)
    order.add_observer(customer2)
    
    # Update order status and notify customers
    order.update_status("Preparing")
    order.update_status("Out for Delivery")
    order.update_status("Delivered")

if __name__ == "__main__":
    main()
