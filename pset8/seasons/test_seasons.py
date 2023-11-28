from seasons import check_date
import pytest

def test_check_date():
    assert check_date("1999-01-01") == "1999-01-01"
    with pytest.raises(ValueError):
        check_date("January 1, 1999")

def test_cal_date():
    with pytest:
        seasons.check_date("1999-01-01")

def test_d_to_t():
    assert seasons.check_date("1999-01-01") == "Nineteen million, nine hundred ninety thousand, one hundred one minutes"
