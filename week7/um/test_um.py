import pytest
from um import count


def test_input():
    assert count("Um, Its a sunny day.") == 1
    assert count("um") == 1
    assert count("Um, gracias, um...see you later") == 2
    assert count("Um!?") == 1
