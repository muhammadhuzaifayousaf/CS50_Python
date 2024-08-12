import pytest
from working import convert

def test_conversion():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("1:00 PM to 11:59 PM") == "13:00 to 23:59"

    with pytest.raises(ValueError):
        convert("9:00AM - 5:00PM")
    with pytest.raises(ValueError):
        convert("9 to 5")
    with pytest.raises(ValueError):
        convert("25:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("12:60 PM to 5:00 PM")
