#introducing OOP


class LifetimeCalculator:

    GOV_BOOST = 0.25
    FIRST_YEAR_AER = 0.0445
    SUBSEQUENT_AER = 0.0280

    def __init__(self, contribution, years):
        self.contribution = contribution
        self.years =  years

    def govermentBoost(self):
        return self.contribution * self.GOV_BOOST

    def firstYear_AER(self, balance):
        # Geometric mean, because interest goews exponentially, so we must use
        # geometric breakdown, which extracts the fractional power (1/12)
        x = 1 + (self.FIRST_YEAR_AER)
        AER = pow(x, 1 / 12) - 1
        return balance * AER

    def subsequent_AER(self, balance):
        x = 1 + (self.SUBSEQUENT_AER)
        AER = pow(x, 1 / 12) - 1
        return balance * AER

    def calculate_monthly(self):
        account_balance = 0.0
        contribution_balance = 0.0
        interest_balance = 0.0
        boost_balance = 0.0
        
        accrued_contribution = []
        accrued_interest = []
        accrued_boost = []
        accured_contribution_with_interest_data = []
        accrued_contribution_without_interest_data = []
        """
        Month x > 1
        1. contribution is added to balance
        2. contribution GOV_BOOST calculated and added to balance
        3. (contribution+GOV_BOOST) interest calculated and added to balance
        """
        months = (self.years * 12) + 1
        boost = self.govermentBoost()

        for month in range(1, months):
            account_balance += self.contribution

            contribution_balance += self.contribution
            accrued_contribution.append(contribution_balance)

        
            if month == 1:
                firstYear_interest = self.firstYear_AER(account_balance)
                account_balance += firstYear_interest
                accrued_interest.append(firstYear_interest)
                

            elif month <= 12:
                account_balance += boost
                boost_balance += boost
                firstYear_interest = self.firstYear_AER(account_balance)
                account_balance += firstYear_interest
                accrued_interest.append(firstYear_interest)

            else:
                account_balance += boost
                boost_balance += boost
                subsequent_interest = self.subsequent_AER(account_balance)
                account_balance += subsequent_interest
                accrued_interest.append(subsequent_interest)

            print(account_balance)
            accrued_boost.append(boost_balance)
            accured_contribution_with_interest_data.append(account_balance)
            accrued_contribution_without_interest_data.append(contribution_balance)

        print ("final account_balance", account_balance)

        print(account_balance)
        print(accrued_contribution)
        print(accrued_interest)
        print(accrued_boost)
        print(accured_contribution_with_interest_data)
        print(accrued_contribution_without_interest_data)
     
        
        return (
                f"{account_balance:.2f}",
                accrued_interest, 
                accrued_boost,
                accured_contribution_with_interest_data,
                accrued_contribution_without_interest_data)
