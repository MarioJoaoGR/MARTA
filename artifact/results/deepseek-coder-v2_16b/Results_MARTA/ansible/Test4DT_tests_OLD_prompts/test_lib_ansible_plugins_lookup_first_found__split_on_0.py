
import pytest
from ansible.plugins.lookup.first_found import _split_on


def test_splitting_empty_list():
    terms = []
    expected = []
    result = _split_on(terms)
    assert result == expected

