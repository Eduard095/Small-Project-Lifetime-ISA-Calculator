#introducing OOP


class LifetimeCalculator:

    GOV_BOOST = 0.25
    FIRT_YEAR_AER = 0.0445
    SUBSEQUENT_AER = 0.028

    account_balance = 0.0
    contribution_balance = 0.0
    interest_balance = 0.0
    boost_balance = 0.0
    
    accrued_contribution = []
    accrued_interest = []
    accrued_boost = []
    accured_contribution_with_interest_data = []
    accrued_contribution_without_interest_data = []


    def __init__(self, contribution, years, frequency):
        self.contribution = contribution
        self.years =  years

    def govermentBoost(self):
        return self.contribution * self.GOV_BOOST

    def firstYear_AER(self):
        # Geometric mean, because interest goews exponentially, so we must use
        # geometric breakdown, which extracts the fractional power (1/12)
        x = 1 + (self.FIRT_YEAR_AER)
        AER = pow(x, 1 / 12) - 1
        return self.account_balance * AER

    def subsequent_AER(self):
        x = 1 + (self.SUBSEQUENT_AER)
        AER = pow(x, 1 / 12) - 1
        return self.account_balance * AER

    def calculate_monthly(self):

        months = (self.years * 12) + 1
        boost = float(self.govermentBoost())

        for month in range(1, months):
            self.account_balance += self.contribution
            self.contribution_balance += self.contribution
            self.accrued_contribution.append(self.contribution_balance)
            self.boost_balance += boost
            self.accrued_boost.append(self.boost_balance)

            if month == 1:
                self.account_balance += float(self.firstYear_AER())
                self.accrued_interest.append(self.firstYear_AER())
                

            elif month <= 12:
                self.account_balance += boost
                self.account_balance += float(self.firstYear_AER())
                self.accrued_interest.append(self.firstYear_AER())

            else:
                self.account_balance += boost
                self.account_balance += float(self.subsequent_AER())
                self.accrued_interest.append(self.subsequent_AER())

            print(self.account_balance)
            self.accured_contribution_with_interest_data.append(self.account_balance)
            self.accrued_contribution_without_interest_data.append(self.contribution_balance)

        print ("final account_balance", self.account_balance)
        print(self.accrued_contribution)
        print(self.accrued_interest)
        print(self.accrued_boost)
        print(self.accured_contribution_with_interest_data)
        print(self.accrued_contribution_without_interest_data)
        
        return (self.accrued_contribution, 
                self.accrued_interest, 
                self.accrued_boost,
                self.accured_contribution_with_interest_data,
                self.accrued_contribution_without_interest_data)
        
    def calculate_yearly(self,contribution, years):
        months = self.years * 12
        self.account_balance += float(self.govermentBoost(self.contribution)) * (months - 2)
        pass


#test1 = LifetimeCalculator(contribution=50,years=1, frequency=1)
#result = test1.calculate_monthly()