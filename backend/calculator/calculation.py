from backend.calculator.goverment_boost import gov_boost
from backend.calculator.interest import AER_after_first_year, first_year_monthly_AER


def monthly_calculations(contribution, years):
    balance = 0
    contribution_only = 0
    contribution_with_interest_data = []
    contribution_without_interest_data = []
    interest_only = []
    boost_only = []
    boost_balance = 0

    count = years * 12

    

    for month in range(count):
        month += 1
        print(balance)
        balance += contribution
        contribution_only += contribution
        boost = float(gov_boost(contribution))
        
        if month == 1:
            first_year_interest = float(first_year_monthly_AER(balance))
            balance += first_year_interest
            interest_only.append(first_year_interest)
            
        elif month <= 12:
            balance += boost
            boost_balance += boost
            first_year_interest = float(first_year_monthly_AER(balance))
            balance += first_year_interest
            interest_only.append(first_year_interest)
            

    
        elif month > 12:
            balance += boost
            boost_balance += boost
            after_first_year_interest = float(AER_after_first_year(balance))
            balance += after_first_year_interest
            interest_only.append(after_first_year_interest)

            
        contribution_without_interest_data.append(contribution_only)
        contribution_with_interest_data.append(balance)
        boost_only.append(boost_balance)
    
    print(balance)
    print("Final Balance", f"{balance:.2f}")
    return f"{balance:.2f}", contribution_with_interest_data, contribution_without_interest_data,interest_only, boost_only
