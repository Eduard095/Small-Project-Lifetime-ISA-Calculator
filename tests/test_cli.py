#testing zone
import pytest
from backend.cli import main
from backend.calculator.interest import first_year_monthly_AER, AER_after_first_year
from backend.calculator.calculation import monthly_calculations


#1. check contribution is 10 <= x <= 333
#2. check years for now, years < 30
#3 make sure to return the correct values
def test_main(monkeypatch):
    #the two responses that 
    inputs = iter(["200", "5"])

    #replace the real input() with one that gives me the next fake input
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))

    contribution, years = main()

    #both argument outcomes should be the same values after function
    assert contribution == 200.0
    assert years == 5
    # both argument outcomes should still be float and int data types
    assert isinstance(contribution,float)
    assert isinstance(years, int)

#testing out for non numeric inputs in "contribution"
def test_non_numeric_contribution_main(monkeypatch):
    inputs = iter(["abc", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    result = main()
    assert result == 0

#testing out decimal points inputs in "years"
def test_decimal_years_main(monkeypatch):
    inputs = iter(["200", "5.5"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    result = main()
    assert result == 0






    
