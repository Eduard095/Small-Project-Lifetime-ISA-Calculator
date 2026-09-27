import pytest
from backend.calculator.calculation import monthly_calculations


# check if function calculates 12 months correctly with only 4.45% AER
def test_one_year_monthly_calculations():
    result = monthly_calculations(contribution=50, years=1)

    assert result == pytest.approx(754.9016288318421)
