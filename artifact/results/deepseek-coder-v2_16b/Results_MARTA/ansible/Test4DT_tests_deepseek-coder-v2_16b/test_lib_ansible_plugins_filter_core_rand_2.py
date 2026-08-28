
import pytest
from ansible.plugins.filter.core import rand
from random import Random, SystemRandom
from ansible.errors import AnsibleFilterError

def test_valid_case_1():
    result = rand(None, 10, start=0, step=2)
    assert isinstance(result, int), "Expected an integer"
    assert 0 <= result < 10 and result % 2 == 0, f"Expected a number between 0 and 10 with a step of 2, got {result}"

def test_valid_case_2():
    result = rand(None, [1, 2, 3, 4, 5])
    assert isinstance(result, int), "Expected an integer"
    assert result in [1, 2, 3, 4, 5], f"Expected a number from the list [1, 2, 3, 4, 5], got {result}"

def test_error_case():
    with pytest.raises(AnsibleFilterError):
        rand(None, 'not an integer', start=0, step=1)
