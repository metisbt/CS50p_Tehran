from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("0/1") == 0
    assert convert("1/1") == 100
    assert convert("1/100") == 1
    assert convert("1/2") == 50

    with pytest.raises(ValueError):
        convert("x/y")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(1) == "E"
    assert gauge(77) == "77%"
    assert gauge(99) == "F"
