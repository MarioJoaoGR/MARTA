
import pytest
from unittest.mock import patch
from ansible.module_utils.common.collections import is_iterable

def count(seq):
    """Returns a dictionary with the number of appearances of each element in the iterable.

    This function counts the occurrences of each element in the provided sequence and returns them as a dictionary. It is designed to be used when Python 2.6.* is still supported, as `collections.Counter` may not be available on such versions. When support for Python < 2.7 is dropped, this function should be deprecated and replaced with an equivalent implementation that leverages modern language features or the standard library's capabilities.

    Parameters:
        seq (Iterable): The sequence of elements to count. This can be a list, tuple, set, string, etc., but must support iteration.

    Returns:
        dict: A dictionary where keys are the elements from the iterable and values are their counts.

    Raises:
        Exception: If the provided argument is not an iterable, an exception is raised with the message "Argument provided is not an iterable".

    Examples:
        >>> count([1, 2, 2, 3, 3, 3])
        {1: 1, 2: 2, 3: 3}
        >>> count("hello")
        {'h': 1, 'e': 1, 'l': 2, 'o': 1}
        >>> count((1, 2, 2, 3, 3, 3))
        {1: 1, 2: 2, 3: 3}
    """
    if not is_iterable(seq):
        raise Exception('Argument provided is not an iterable')
    counters = dict()
    for elem in seq:
        counters[elem] = counters.get(elem, 0) + 1
    return counters


def test_none_sequence():
    with patch('ansible.module_utils.common.collections.is_iterable', return_value=False):
        with pytest.raises(Exception) as excinfo:
            count(None)
        assert str(excinfo.value) == "Argument provided is not an iterable"