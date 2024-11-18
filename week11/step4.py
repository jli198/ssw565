'''
Step 4: Add Income Calculation for Each State
Now, assume we also need a calculate_income function that varies by state. In this step, each state needs both calculate_tax and calculate_income.
'''

# Clone-and-Own Approach

# Tax calculation for each state
def calculate_tax(amount, state="Default"):
    if state == "Delaware":
        return calculate_delaware_tax(amount)
    elif state == "Texas":
        return calculate_texas_tax(amount)
    else:
        return amount * 0.05  # Default tax rate

def calculate_delaware_tax(amount):
    return amount * 0.06

def calculate_texas_tax(amount):
    return amount * 0.04

# Income calculation for each state
def calculate_income(base_income, state="Default"):
    if state == "Delaware":
        return calculate_delaware_income(base_income)
    elif state == "Texas":
        return calculate_texas_income(base_income)
    else:
        return base_income  # Default income

def calculate_delaware_income(base_income):
    return base_income * 1.05  # Delaware-specific income adjustment

def calculate_texas_income(base_income):
    return base_income + 100  # Texas-specific income adjustment

# Example usage
print("Default Tax:", calculate_tax(1000))
print("Default Income:", calculate_income(50000))

print("Delaware Tax:", calculate_tax(1000, "Delaware"))
print("Delaware Income:", calculate_income(50000, "Delaware"))

print("Texas Tax:", calculate_tax(1000, "Texas"))
print("Texas Income:", calculate_income(50000, "Texas"))

# Factory Pattern Approach

# Base Tax and Income Calculator
class TaxCalculator:
    def calculate_tax(self, amount):
        return amount * 0.05  # Default tax rate

    def calculate_income(self, base_income):
        return base_income  # Default income calculation

# Delaware-Specific Calculator
class DelawareTaxCalculator(TaxCalculator):
    def calculate_tax(self, amount):
        return amount * 0.06  # Delaware-specific tax rate

    def calculate_income(self, base_income):
        return base_income * 1.05  # Delaware-specific income adjustment

# Texas-Specific Calculator
class TexasTaxCalculator(TaxCalculator):
    def calculate_tax(self, amount):
        return amount * 0.04  # Texas-specific tax rate

    def calculate_income(self, base_income):
        return base_income + 100  # Texas-specific income adjustment

# Factory Class
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
print("Default Income:", calculator.calculate_income(50000))

calculator = TaxCalculatorFactory.get_calculator("Delaware")
print("Delaware Tax:", calculator.calculate_tax(1000))
print("Delaware Income:", calculator.calculate_income(50000))

calculator = TaxCalculatorFactory.get_calculator("Texas")
print("Texas Tax:", calculator.calculate_tax(1000))
print("Texas Income:", calculator.calculate_income(50000))
'''
Final Comparison
At this final stage:

Clone-and-Own: The number of functions increases, making it harder to manage as each state has independent calculate_tax and calculate_income functions. The conditional complexity in calculate_tax and calculate_income also increases, leading to code that’s harder to maintain.
Factory Pattern: The addition of calculate_income is handled smoothly within each subclass, preserving encapsulation and modularity. Each state’s variations are neatly organized within a single class, and adding new states or methods is straightforward.
This progression highlights the scalability and maintainability of the factory pattern, especially as the complexity of state-specific logic grows. The factory pattern keeps state-specific logic contained, reducing redundancy and making the code easier to extend and maintain.
'''