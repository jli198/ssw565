'''
Step 3: Add Texas-Specific Tax Calculation
Now, Texas also has a unique tax rate. We’ll follow the same approach by adding another function in clone-and-own and a new subclass in the factory pattern.
'''

# Clone-and-Own Approach

def calculate_tax(amount, state="Default"):
    if state == "Delaware":
        return calculate_delaware_tax(amount)
    elif state == "Texas":
        return calculate_texas_tax(amount)
    else:
        return amount * 0.05  # Default tax rate

def calculate_delaware_tax(amount):
    return amount * 0.06  # Delaware-specific 6% tax rate

def calculate_texas_tax(amount):
    return amount * 0.04  # Texas-specific 4% tax rate

# Example usage
print("Default Tax:", calculate_tax(1000))
print("Delaware Tax:", calculate_tax(1000, "Delaware"))
print("Texas Tax:", calculate_tax(1000, "Texas"))

# Factory Pattern Approach

class TaxCalculator:
    def calculate_tax(self, amount):
        return amount * 0.05  # Default tax rate

class DelawareTaxCalculator(TaxCalculator):
    def calculate_tax(self, amount):
        return amount * 0.06  # Delaware-specific tax rate

class TexasTaxCalculator(TaxCalculator):
    def calculate_tax(self, amount):
        return amount * 0.04  # Texas-specific tax rate

class TaxCalculatorFactory:
    @staticmethod
    def get_calculator(state="Default"):
        if state == "Delaware":
            return DelawareTaxCalculator()
        elif state == "Texas":
            return TexasTaxCalculator()
        else:
            return TaxCalculator()

# Example usage
calculator = TaxCalculatorFactory.get_calculator()
print("Default Tax:", calculator.calculate_tax(1000))

calculator = TaxCalculatorFactory.get_calculator("Delaware")
print("Delaware Tax:", calculator.calculate_tax(1000))

calculator = TaxCalculatorFactory.get_calculator("Texas")
print("Texas Tax:", calculator.calculate_tax(1000))

'''
Comparison at this Stage
With multiple variations:

Clone-and-Own: Begins to introduce multiple independent functions (calculate_delaware_tax, calculate_texas_tax), increasing conditional complexity in calculate_tax.
Factory Pattern: Adds another subclass (TexasTaxCalculator) without changing the main calculate_tax method, keeping each state’s logic encapsulated in separate classes.
'''