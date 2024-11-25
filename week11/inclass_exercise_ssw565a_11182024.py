# in-class exercise
from clone_and_own import calculator


def calculater_interests(amount, state = 'Default'):
    if state == 'DE':
        return amount * 0.06
    elif state == 'TX':
        return (amount+500) * 0.04
    else:
        return amount * 0.05 # 5% interest rate

print('DE interests is', calculater_interests(1000,'DE'))
print('default interests is', calculater_interests(1000))
print('TX interests is', calculater_interests(1000, 'TX'))


class InterestsCalculator:
    def calculate_interests(self, amount):
        return amount*0.05

class DEInterestsCalculator:
    def calculate_interests(self, amount, income=0):
        print('income is', income)
        if income >= 20000:
            print('income is higher than 20000', income)
            return amount * 0.06
        else:
            print('income is lower than 20000', income)
            return (amount+500)*0.06

class TxInterestsCalculator:
    def calculate_interests(self, amount):
        return (amount+1000)*0.04

class InterestCalculatorFactory:
    @staticmethod
    def get_calculator(state='Default'):
        if state == 'DE':
            return DEInterestsCalculator()
        else:
            return InterestsCalculator()

calculator_de = InterestCalculatorFactory.get_calculator(state = 'DE')
print('DE New Interests is', calculator_de.calculate_interests(1000, 30000))

# calculator = InterestCalculatorFactory.get_calculator(state = 'NJ')
# print('NJ Interests is', calculator.calculate_interests(1000))

#
# calculator = InterestCalculatorFactory.get_calculator(state = 'Tx')
# print('Tx Interests is', calculator.calculate_interests(1000))