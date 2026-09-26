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