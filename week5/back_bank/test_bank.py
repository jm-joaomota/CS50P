from bank import value
import pytest


def test_value():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hi world") == 20
    assert value("HI World") == 20
    assert value("Olá") == 100
    assert value("OLÁ") == 100
