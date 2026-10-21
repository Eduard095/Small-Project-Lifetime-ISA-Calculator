import pytest

from backend.calculator.calculation import firstYear_AER, subsequent_AER


# testing out the if the mathematical formula to calculate AER for the first year is correct
def test_formula_firstYear_AER():
    contribution = 100
    AER = firstYear_AER(contribution)
    result = AER / contribution
    # the formula should approximate 0.0036...
    assert result == pytest.approx(0.0036347816898771867)


# Testing out with multiple if interest is correctly calculated on each test case
@pytest.mark.parametrize("contribution", [1, 50, 100, 500, 1000, 5000, 10000, 20000])
def test_function_firstYear_AER(contribution):
    # rate calculates just the interst rate so when * to contribution it correctly calculates the interest of the given contribution
    rate = firstYear_AER(1)
    # The function should correctly calculate each test case
    assert firstYear_AER(contribution) == pytest.approx(contribution * rate)


# formula test for the AER after first year boost
def test_formula_subsequent_AER():
    contribution = 100
    AER = subsequent_AER(contribution)
    result = AER / contribution
    assert result == pytest.approx(0.0023039138595752906)


# testing multiple test cases for this AER calculation
@pytest.mark.parametrize("contribution", [1, 50, 100, 500, 1000, 5000, 10000, 20000])
def test_function_subsequent_AER(contribution):
    rate = subsequent_AER(1)

    assert subsequent_AER(contribution) == pytest.approx(contribution * rate)
