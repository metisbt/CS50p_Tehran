from plates import is_valid


def test_1():
    assert is_valid("66gy76") == False
    assert is_valid("1A3") == False
    assert is_valid("AA3") == True

def test_2():
    assert is_valid("C") == False
    assert is_valid("ASDIKQF") == False
    assert is_valid("LKJHGF") == True

def test_3():
    assert is_valid("123456") == False
    assert is_valid("123KF") == True
    assert is_valid("CCC012") == False
    assert is_valid("WE12V4") == False
    assert is_valid("EF12PO") == False
    assert is_valid("AMU567") == True

def test_4():
    assert is_valid("12#$ )") == False
    assert is_valid(" 9A^$O") == False
    assert is_valid("/A#$F.") == False
    assert is_valid("AMU567") == True
