from project import insert_data, get_data, check_locate, is_connected
import pytest

def test_insert_data():
    l = 'telegram'
    user = 'mahdi'
    pw = '1234'

    assert insert_data(user, pw, l) == insert_data('mahdi', '1234', 'telegram')

def test_get_data():
    l = 'telegram'
    assert get_data(l) == get_data('telegram')


def test_check_locate():
    assert check_locate('telegram') == True

def test_is_connected():
    assert is_connected('database.db') == True