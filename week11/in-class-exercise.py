# in-class exercise

def calculator_interests(amount, state = 'Default'):
  if state == 'DE':
    return amount * 0.06
  elif state == 'TX':
    return (amount+500) * 0.04
  else:
    return amount * 0.05  # 5% interest rate

print('DE interset is', calculator_interests(1000, 'DE'))
print('default interests is', calculator_interests(1000))
print('DE interset is', calculator_interests(1000, 'TX'))

class InterestsCalculator:
  def calculate_interests(self, amount):
    return amount*0.05

class DEInterestsCalculator:
  def calculate_interests(self, amount):
    return (amount+500)*0.06

class TxInterestsCalculator:
  def calculate_interests(self, amount):
    return (amount+1000)*0.04
  
class InterestCalculatorFactory:
  @staticmethod
  def get_calculator(state='Default'):
    if state == 'DE':
      return DEInterestsCalculator()
    elif state == 'TX':
      return TxInterestsCalculator()
    else:
      return InterestsCalculator()
    
calculator = InterestCalculatorFactory.get_calculator(state= 'DE')
print('DE Interest is', calculator.calculate_interests(1000))

calculator = InterestCalculatorFactory.get_calculator(state= 'NJ')
print('NJ Interest is', calculator.calculate_interests(1000))

calculator = InterestCalculatorFactory.get_calculator(state= 'TX')
print('TX Interest is', calculator.calculate_interests(1000))