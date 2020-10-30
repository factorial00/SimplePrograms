# Python3 program to find compound 
# interest for given values. 
  
def compound_interest(principle, rate, time): 
  
    # Calculates compound interest  
    Amount = principle * (pow((1 + rate / 100), time)) 
    CI = Amount - principle 
    print 'Compound interest is', CI
  
compound_interest(float(input('Enter the principle: ')), float(input('Enter the rate: ')), float(input('Enter the time: ')))