
import pytest
from mimesis.random import Random
from typing import List

def test_valid_randints():
    rand_gen = Random()
    result = rand_gen.randints(amount=5, a=1, b=100)
    assert isinstance(result, list), "Expected a list"
    assert len(result) == 5, "Expected exactly 5 integers"
    for num in result:
        assert isinstance(num, int), "All elements should be integers"
        assert 1 <= num <= 100, f"Number {num} is out of the expected range [1, 100]"

def test_invalid_randints():
    rand_gen = Random()
    with pytest.raises(ValueError):
        rand_gen.randints(amount=0, a=1, b=100)

def test_negative_range_randints():
    rand_gen = Random()
    result = rand_gen.randints(amount=5, a=-50, b=50)
    assert isinstance(result, list), "Expected a list"
    assert len(result) == 5, "Expected exactly 5 integers"
    for num in result:
        assert isinstance(num, int), "All elements should be integers"
        assert -50 <= num <= 50, f"Number {num} is out of the expected range [-50, 50]"
