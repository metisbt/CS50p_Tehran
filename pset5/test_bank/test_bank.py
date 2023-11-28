from bank import value

def test_value_case():
    assert value("hello") == 0
    assert value("HELLO") == 0


def test_value_first():
    assert value("how are you?") == 20
    assert value("ha ha ha") == 20


def test_value_fail():
    assert value("What do you do?") == 100
    assert value("mahdi") == 100
