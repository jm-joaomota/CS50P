from twitter import shorten
import pytest


def test_lower_vowels():
    assert shorten("a") == ""
    assert shorten("e") == ""
    assert shorten("i") == ""
    assert shorten("o") == ""
    assert shorten("u") == ""


def test_upper_vowels():
    assert shorten("A") == ""
    assert shorten("E") == ""
    assert shorten("I") == ""
    assert shorten("O") == ""
    assert shorten("U") == ""
