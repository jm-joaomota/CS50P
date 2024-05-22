from seasons import convert
import pytest

def test_date():
    assert convert("1999-01-01") == "Thirteen million, three hundred fifty-three thousand, one hundred twenty minutes"
    assert convert("1994-03-19") == "Fifteen million, eight hundred seventy-one thousand, six hundred eighty minutes"
