# direction Implementation 

class Pizza:
    def __init__(self, crust, sauce, cheese, toppings=None):
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings or []

    def __str__(self):
        return f"Pizza with {self.crust} crust, {self.sauce} sauce, {self.cheese} cheese, and toppings: {', '.join(self.toppings)}."

# Client Code
def main():
    # Directly constructing a Pizza
    margherita = Pizza("thin", "tomato", "mozzarella", ["basil"])
    pepperoni = Pizza("thick", "barbecue", "cheddar", ["pepperoni"])

    print(margherita)
    print(pepperoni)

if __name__ == "__main__":
    main()



# Builder Implementation

class Pizza:
    def __init__(self):
        self.crust = None
        self.sauce = None
        self.cheese = None
        self.toppings = []

    def __str__(self):
        return f"Pizza with {self.crust} crust, {self.sauce} sauce, {self.cheese} cheese, and toppings: {', '.join(self.toppings)}."

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_crust(self, crust):
        self.pizza.crust = crust
        return self

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self

    def add_cheese(self, cheese):
        self.pizza.cheese = cheese
        return self

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self

    def get_pizza(self):
        return self.pizza

# Client Code
def main():
    builder = PizzaBuilder()
    margherita = builder.set_crust("thin").set_sauce("tomato").add_cheese("mozzarella").add_topping("basil").get_pizza()
    pepperoni = builder.set_crust("thick").set_sauce("barbecue").add_cheese("cheddar").add_topping("pepperoni").get_pizza()

    print(margherita)
    print(pepperoni)

if __name__ == "__main__":
    main()
