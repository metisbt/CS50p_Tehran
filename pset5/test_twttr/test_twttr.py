from twttr import shorten

def test_shorten():
    assert shorten("aeiquo") == ""
    assert shorten("AEUIO") == ""
    assert shorten("ezzat") == "zzt"
    assert shorten("mahdi") == "mhd"
    assert shorten("1234 : wasrtg") == "1234 : wsrtg"
