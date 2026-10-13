#introducing OOP


class LifetimeCalculator:

    GOV_BOOST = 0.25
    FIRT_YEAR_AER = 0.0445
    SUBSEQUENT_AER = 0.028

    balance  = 0.0

    accrued_contribution = []
    accrued_interest = []
    accrued_boost = []
    accrued_contribution_without_interest_data = []
    accured_contribution_with_interest_data = []


    def __init__(self, contribution, years, frequency):
        self.contribution = contribution
        self.years =  years

    def govermentBoost(self):
        return self.contribution * self.GOV_BOOST

    # Geometric mean, because interest goews exponentially, so we must use
    # geometric breakdown, which extracts the fractional power (1/12)
    def firstYear_AER(self):
        x = 1 + (self.FIRT_YEAR_AER)
        AER = pow(x, 1 / 12) - 1
        return self.balance * AER

    def subsequent_AER(self):
        x = 1 + (self.SUBSEQUENT_AER)
        AER = pow(x, 1 / 12) - 1
        return self.balance * AER


    def calculate_monthly(self):

        months = (self.years * 12) + 1
        boost = float(self.govermentBoost())

        for month in range(1, months):
            print(self.balance)
            self.balance += self.contribution

            if month == 1:
                self.balance += float(self.firstYear_AER())

            elif month <= 12:
                self.balance += boost
                self.balance += float(self.firstYear_AER())

            else:
                self.balance += boost
                self.balance += float(self.subsequent_AER())

        return print ("final balance", self.balance)
        
    

    def calculate_yearly(self,contribution, years):
        months = self.years * 12
        self.balance += float(self.govermentBoost(self.contribution)) * (months - 2)
        pass


test1 = LifetimeCalculator(contribution=50,years=1, frequency=1)
result = test1.calculate_monthly()