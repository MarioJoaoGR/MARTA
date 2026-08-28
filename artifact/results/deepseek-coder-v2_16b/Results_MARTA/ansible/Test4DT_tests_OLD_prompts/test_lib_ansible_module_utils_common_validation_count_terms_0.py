
import pytest
from unittest.mock import patch

def count_terms(terms, parameters):
    """Count the number of occurrences of a key in a given dictionary

    :arg terms: String or iterable of values to check
    :arg parameters: Dictionary of parameters

    :returns: An integer that is the number of occurrences of the terms values
        in the provided dictionary.
    """

    if not isinstance(terms, (list, tuple)):
        terms = [terms]

    return len([term for term in terms if term in parameters])

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

# Test cases
@pytest.mark.parametrize("terms, parameters, expected", [
    ("hello", {"hello": 1, "world": 2}, 1),
    (["hello", "world"], {"hello": 1, "world": 2, "foo": 3}, 2),
    (["hello", "foo"], {"bar": 4, "baz": 5}, 0)
])
def test_count_terms(terms, parameters, expected):
    assert count_terms(terms, parameters) == expected
