#testing zone
import pytest
from index import user_input, first_year_monthly_AER


#1. check contribution is 10 <= x <= 333
#2. check years for now, years < 30
#3 make sure to return the correct values
def test_user_input(monkeypatch):
    #the two responses that 
    inputs = iter(["200", "5"])

    #replace the real input() with one that gives me the next fake input
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    contribution, years = user_input()

    #both argument outcomes should be the same values after function
    assert contribution == 200.0
    assert years == 5
    # both argument outcomes should still be float and int data types
    assert isinstance(contribution,float)
    assert isinstance(years, int)

#testing out for non numeric inputs in "contribution"
def test_non_numeric_contribution_user_input(monkeypatch):
    inputs = iter(["abc", "5"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))

    with pytest.raises(ValueError):
        user_input()

#testing out decimal points inputs in "years"
def test_decimal_years_user_input(monkeypatch):
    inputs = iter(["200", "5.5"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))

    with pytest.raises(ValueError):
        user_input()


#testing out the if the mathematical formula to calculate AER for the first year is correct
def test_formula_first_year_monthly_AER():
    contribution = 100
    AER = first_year_monthly_AER(contribution)
    result = AER / contribution
    # the formula should approximate 0.0036...
    assert result == pytest.approx(0.0036347816898771867)

#Testing out with multiple if interest is correctly calculated on each test case
@pytest.mark.parametrize("contribution", [1,50,100,500,1000,5000,10000,20000])
def test_function_first_year_monthly_AER(contribution):
    #rate calculates just the interst rate so when * to contribution it correctly calculates the interest of the given contribution
    rate = first_year_monthly_AER(1)
    #The function should correctly calculate each test case
    assert first_year_monthly_AER(contribution) == pytest.approx(contribution * rate)
