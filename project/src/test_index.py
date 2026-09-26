#testing zone
import pytest
from index import user_input, first_year_monthly_AER, AER_after_first_year, monthly_calculations, main


#1. check contribution is 10 <= x <= 333
#2. check years for now, years < 30
#3 make sure to return the correct values
def test_main(monkeypatch):
    #the two responses that 
    inputs = iter(["200", "5"])

    #replace the real input() with one that gives me the next fake input
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

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
    assert result == -1

#testing out decimal points inputs in "years"
def test_decimal_years_main(monkeypatch):
    inputs = iter(["200", "5.5"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))
    result = main()
    assert result == -1


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

#formula test for the AER after first year boost
def test_formula_AER_after_first_year():
    contribution = 100
    AER = AER_after_first_year(contribution)
    result = AER / contribution
    assert result == pytest.approx(0.0023039138595752906)

#testing multiple test cases for this AER calculation
@pytest.mark.parametrize("contribution", [1,50,100,500,1000,5000,10000,20000])
def test_function_AER_after_first_year(contribution):
    rate = AER_after_first_year(1)

    assert AER_after_first_year(contribution) == pytest.approx(contribution * rate)


# check if function calculates 12 months correctly with only 4.45% AER
def test_one_year_monthly_calculations():
    result = monthly_calculations(contribution=50, years=1)

    assert result == pytest.approx(754.9016288318421)

    
