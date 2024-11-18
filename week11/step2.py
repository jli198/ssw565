'''
Step 2: Introduce Delaware-Specific Tax Calculation
Now, assume Delaware requires a slightly different tax calculation. Let’s add a calculate_delaware_tax function in clone-and-own and use a subclass in the factory pattern.
'''

# Clone-and-Own Approach

def calculate_tax(amount, state="Default"):
    if state == "Delaware":
        return calculate_delaware_tax(amount)
    else:
        return amount * 0.05  # Default tax rate

def calculate_delaware_tax(amount):
    return amount * 0.06  # Delaware-specific 6% tax rate

# Example usage
print("Default Tax:", calculate_tax(1000))
print("Delaware Tax:", calculate_tax(1000, "Delaware"))

# Factory Pattern Approach

class TaxCalculator:
    def calculate_tax(self, amount):
        return amount * 0.05  # Default tax rate

class DelawareTaxCalculator(TaxCalculator):
    def calculate_tax(self, amount):
        return amount * 0.06  # Delaware-specific tax rate

class TaxCalculatorFactory:
    @staticmethod
    def get_calculator(state="Default"):
        if state == "Delaware":
            return DelawareTaxCalculator()
        else:
            return TaxCalculator()

# Example usage
calculator = TaxCalculatorFactory.get_calculator()
print("Default Tax:", calculator.calculate_tax(1000))

calculator = TaxCalculatorFactory.get_calculator("Delaware")
print("Delaware Tax:", calculator.calculate_tax(1000))

'''
Comparison at this Stage
Clone-and-Own: Adds a separate function calculate_delaware_tax, which is called conditionally.
Factory Pattern: Adds a DelawareTaxCalculator subclass and modifies the factory, keeping Delaware’s logic encapsulated within a subclass.
'''