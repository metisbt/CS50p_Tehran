import pytest
from working import convert


def test_case():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_mixed():
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")


def test_max():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_to():
    with pytest.raises(ValueError):
        convert(" to ")


def test_outh():
    with pytest.raises(ValueError):
        convert("14:00 AM to 14:00 PM")

    with pytest.raises(ValueError):
        convert("0:00 AM to 0:00 PM")

    with pytest.raises(ValueError):
        convert("14 AM to 14 PM")

    with pytest.raises(ValueError):
        convert("0 AM to 0 PM")




def test_outm():
    with pytest.raises(ValueError):
        convert("14:61 AM to 4:60 PM")


def test_ne():
    with pytest.raises(ValueError):
        convert("")



def test_invformate():
    with pytest.raises(ValueError):
        convert("8AM to 9PM")

    with pytest.raises(ValueError):
        convert("3:20 AM 7:30 PM")

    with pytest.raises(ValueError):
        convert("10 AM - 7 PM")

