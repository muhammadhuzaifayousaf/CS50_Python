from datetime import date
import pytest
from seasons import diff


def test_valid_date():
    assert diff(
        "1999-01-01") == "Thirteen million, four hundred seventy-five thousand, five hundred twenty minutes"


def test_invalid_date_format():
    with pytest.raises(SystemExit):
        diff("01-01-1999")


def test_invalid_date_nonexistent():
    with pytest.raises(SystemExit):
        diff("1999-02-30")


def test_leap_year():
    assert diff(
        "2000-02-29") == "Twelve million, eight hundred sixty-four thousand, nine hundred sixty minutes"
