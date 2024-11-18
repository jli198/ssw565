'''
Step 1: All States Use the Same Tax Calculator
Start with a single calculate_tax function, which works for all states. At this point, we don’t need any variations.
'''

# Code Example (Single Function for All States)

def calculate_tax(amount):
    return amount * 0.05  # 5% tax rate for all states

# Example usage
print("Tax:", calculate_tax(1000))

'''
Comparison at this Stage
Both the factory pattern and clone-and-own are unnecessary here because there are no variations.
'''