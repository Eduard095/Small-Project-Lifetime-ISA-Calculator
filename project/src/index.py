#index.py
import math


def user_input():
    contribution = float(input("1. How much will you be contributing monthly?: "))
    years = int(input("2. In how many years do you want to buy your first home?: "))
    return contribution, years

def first_year_monthly_AER(contribution):
    #Geometric mean, because interest goews exponentially, so we must use 
    #geometric breakdown, which extracts the fractional power (1/12)
    x = 1 + (0.0445)
    first_year_AER_rate = pow(x, 1/12) - 1
    return contribution * first_year_AER_rate

def AER_after_first_year(contribution):
    x = 1 + (0.028)
    after_first_year_AER_rate = pow(x, 1/12) - 1
    return contribution * after_first_year_AER_rate

def gov_boost(contribution):
    return contribution * 0.25


def monthly_calculations(contribution, years):
    balance = 0
    count = years * 12
    
    for x in range(count):
        balance += contribution
        interest = float(first_year_monthly_AER(balance))
        boost = float(gov_boost(contribution))
        
        if x < 1:
            balance += interest
            balance += boost
        elif x > 0 and x < 12:
            balance += interest                  
            balance += boost
        elif x >= 12:
            after_interest = float(AER_after_first_year(balance))
            balance+=after_interest
            balance+= boost

    balance -= boost
    return  print("Final Balance", f"{balance:.2f}")

def main():
    contribution, years = user_input()
    monthly_calculations(contribution, years)
    return



if __name__ == "__main__":
    print('''
Welcome to LISA calulator: 
Please provide the following

-------------------------------------------------------
1. How much will you be contributing monthly?
2. In how many years do you want to buy your first home?
-------------------------------------------------------

''')
    main()
    