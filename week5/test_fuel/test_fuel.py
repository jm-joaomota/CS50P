from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/4") == 25


def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("2/1")
