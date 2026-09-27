import pytest
from backend.calculator.interest import first_year_monthly_AER, AER_after_first_year


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