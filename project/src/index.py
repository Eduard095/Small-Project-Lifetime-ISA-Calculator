#index.py

def user_input():
    contribution = float(input("1. How much will you be contributing monthly?: "))
    years = int(input("2. In how many years do you want to buy your first home?: "))
    return contribution, years

def AER_and_IBR(contribution):
    return contribution * 0.045

def AER(contribution):
    return contribution * 0.028

def gov_boost(contribution):
    return contribution * 0.25


def monthly_calculations(contribution, years):
    account = 0
    count = years * 12 - 1
    for x in range(count):
        account += contribution
        if x < 13:
            x1 = AER_and_IBR(account)
            x3 = gov_boost(account)
            total_boost = x1 + x3
            account += total_boost
            print(account)
        if x > 12:
            x2 = AER(contribution)
            x3 = gov_boost(contribution)
            contribution = contribution + x2 + x3 

    return print(f"{account:.2f}")

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
    