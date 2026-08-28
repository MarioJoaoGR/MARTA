
import pytest
from ansible.plugins.filter import mathstuff
from ansible.errors import AnsibleFilterError


def test_min_with_valid_list_kwargs0():
    kwargs = {'a': [3, 1, 4, 1, 5, 9]}
    result = mathstuff.min({}, **kwargs)
    assert result == 1, "Expected the minimum value of the list to be 1"

def test_min_with_valid_list_kwargs1():
    kwargs = {'a': [3, 1, 4, 1, 5, 9]}
    result = mathstuff.min({}, **kwargs)
    assert result == 1, "Expected the minimum value of the list to be 1"
