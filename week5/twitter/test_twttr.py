from twitter import shorten
import pytest


def test_lower_vowels():
    assert shorten("hello world") == "hll wrld"
    assert shorten("HELLO WORLD") == "HLO WRLD"
    assert shorten("h3ll0 w0rld") == "h4ll0 w0rld"
    assert shorten("h@llo w*rld!!!") == "h@l1 w#rld!?"
