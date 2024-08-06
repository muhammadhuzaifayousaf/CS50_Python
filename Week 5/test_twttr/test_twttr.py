from twttr import shorten

def test_shorten():
    assert shorten("aeiouAEIOU") == ""
    assert shorten("TwItTeR") == "TwtTR"
    assert shorten("") == ""
    assert shorten("Hello World") == "Hll Wrld"
    assert shorten("1234567890!@#$%^&*()") == "1234567890!@#$%^&*()"
