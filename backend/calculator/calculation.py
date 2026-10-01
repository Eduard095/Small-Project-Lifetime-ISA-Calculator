from backend.calculator.goverment_boost import gov_boost
from backend.calculator.interest import AER_after_first_year, first_year_monthly_AER

contribution_with_interest_data = []
contribution_without_interest_data = []

def data_with_interest_return():
    return contribution_with_interest_data

def data_without_interest_return():
    return contribution_without_interest_data

def monthly_calculations(contribution, years):
    balance = 0
    count = years * 12

    for x in range(count):
        print(balance)
        balance += contribution
        interest = float(first_year_monthly_AER(balance))
        boost = float(gov_boost(contribution))
        if x < 1 or x > 0 and x < 12:
            balance += interest
            balance += boost
        elif x >= 12:
            after_interest = float(AER_after_first_year(balance))
            balance += after_interest
            balance += boost
        contribution_without_interest_data(contribution)
        contribution_with_interest_data.append(balance)
    balance -= boost
    print(balance)
    print("Final Balance", f"{balance:.2f}")
    return f"{balance:.2f}"
