import pytest

from backend.calculator.calculation import calculate_monthly


# check if function calculates 12 months correctly with only 4.45% AER
def test_one_year_calculate_monthly():
    result = calculate_monthly(contribution=50, years=1)

    assert result == pytest.approx("754.90")
