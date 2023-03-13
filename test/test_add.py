import pytest
import sys
from src.add import add


def test_add_two_positive_numbers():
    assert add(1, 2) == 3
