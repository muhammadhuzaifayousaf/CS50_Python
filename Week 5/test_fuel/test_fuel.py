import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/1") == 100
    assert convert("0/1") == 0

    with pytest.raises(ValueError):
        convert("4/3")

    with pytest.raises(ValueError):
        convert("abc/def")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(75) == "75%"
