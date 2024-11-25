1. Target Interface (Your System's Expected Interface)

Define the interface that your system expects for payment processing.

class PaymentProcessor:
    def process_payment(self, amount):
        """Process the payment for the given amount."""
        raise NotImplementedError("Subclasses must implement this method.")


2. Adaptee (Third-Party Payment Gateway)

This is the third-party library or API you want to integrate. Its interface is different from what your system expects.



class StripePayment:
    def make_payment(self, currency, amount):
        # Simulate Stripe payment processing
        print(f"Processing payment of {currency} {amount} using Stripe.")


3. Adapter (Converts the Adaptee to the Target Interface)

The adapter implements your system's interface (PaymentProcessor) and translates the method calls to the third-party library's methods.

class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe_payment):
        self.stripe_payment = stripe_payment

    def process_payment(self, amount):
        # Convert the amount to the format expected by Stripe (e.g., assume USD)
        currency = "USD"
        self.stripe_payment.make_payment(currency, amount)


4. Client Code (Your Pizza Ordering System)

The client interacts with the PaymentProcessor interface without worrying about the third-party implementation.

class PizzaOrderingSystem:
    def __init__(self, payment_processor):
        self.payment_processor = payment_processor

    def place_order(self, pizza_name, price):
        print(f"Order placed: {pizza_name} for ${price}")
        self.payment_processor.process_payment(price)
        
        
def main():
    # Third-party Stripe payment instance
    stripe_payment = StripePayment()
    
    # Adapter to make Stripe compatible with our system
    stripe_adapter = StripeAdapter(stripe_payment)
    
    # Pizza ordering system using the adapted payment processor
    ordering_system = PizzaOrderingSystem(stripe_adapter)
    
    # Place an order
    ordering_system.place_order("Margherita Pizza", 15.99)

if __name__ == "__main__":
    main()



How the Adapter Pattern Helps
Seamless Integration:
The adapter bridges the gap between your system's PaymentProcessor interface and the third-party StripePayment class.
No changes are required in the Pizza Ordering System's code.
Flexibility:
If you decide to switch to another payment gateway (e.g., PayPal), you only need to create a new adapter.
Decoupling:
Your system remains decoupled from the specifics of the third-party payment gateway.
Example Extension
Add another adapter for a different payment gateway like PayPal:



class PayPalPayment:
    def send_payment(self, amount):
        print(f"Processing payment of ${amount} using PayPal.")

class PayPalAdapter(PaymentProcessor):
    def __init__(self, paypal_payment):
        self.paypal_payment = paypal_payment

    def process_payment(self, amount):
        self.paypal_payment.send_payment(amount)


Switching to PayPal in the PizzaOrderingSystem would only require:



paypal_payment = PayPalPayment()
paypal_adapter = PayPalAdapter(paypal_payment)
ordering_system = PizzaOrderingSystem(paypal_adapter)
ordering_system.place_order("Pepperoni Pizza", 18.99)

