from jar import Jar
import pytest

def test_init():
    jartest = Jar(10, 9)
    assert jartest.capacity == 10
    assert jartest.size == 9

    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"

    jar.withdraw(1)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    test1 = Jar(10)
    test1.deposit(1)
    assert test1.size == 1

    check1 = Jar(12, 11)
    with pytest.raises(ValueError):
        check1.deposit(2)


def test_withdraw():
    jtest1 = Jar(4)
    jtest1.deposit(3)
    jtest1.withdraw(2)
    assert jtest1.size == 1

    cjar = Jar(12, 11)
    with pytest.raises(ValueError):
        cjar.withdraw(12)