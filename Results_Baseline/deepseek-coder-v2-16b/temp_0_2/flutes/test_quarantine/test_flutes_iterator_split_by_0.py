
import pytest
from typing import List, Iterable, Iterator

# Function under test  
def split_by(iterable: Iterable[A], empty_segments: bool = False, *, criterion=None, separator=None) -> Iterator[List[A]]:
    r"""Split a list into sub-lists by dropping certain elements. Exactly one of ``criterion`` and ``separator`` must be
    specified. For example:

    .. code:: python

        >>> list(split_by(range(10), criterion=lambda x: x % 3 == 0))
        [[1, 2], [4, 5], [7, 8]]

        >>> list(split_by(" Split by: ", empty_segments=True, separator='.'))
        [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]

    :param iterable: The list to split.
    :param empty_segments: If ``True``, include an empty list in cases where two adjacent elements satisfy
        the criterion.
    :param criterion: The criterion to decide whether to drop an element.
    :param separator: The separator for sub-lists. An element is dropped if it is equal to ``parameter``.
    :return: List of sub-lists.
    """
    if not ((criterion is None) ^ (separator is None)):
        raise ValueError("Exactly one of `criterion` and `separator` should be specified")
    if criterion is None:
        criterion = lambda x: x == separator
    group = []
    for x in iterable:
        if not criterion(x):
            group.append(x)
        else:
            if len(group) > 0 or empty_segments:
                yield group
            group = []
    if len(group) > 0 or empty_segments:
        yield group  

# Test case  
def test_split_by_separator():
    string = " Split by: "
    result = list(split_by(string, empty_segments=True, separator='.'))
    assert result == [[], ['S', 'p', 'l', 'i', 't'], ['b', 'y', ':'], []]

def test_split_by_empty_segments():
    numbers = range(10)
    result = list(split_by(numbers, criterion=lambda x: x % 3 == 0, empty_segments=True))
    assert result == [[1, 2], [4, 5], [7, 8]]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_split_by_0
flutes/Test4DT_tests/test_flutes_iterator_split_by_0.py:6:32: E0602: Undefined variable 'A' (undefined-variable)
flutes/Test4DT_tests/test_flutes_iterator_split_by_0.py:6:118: E0602: Undefined variable 'A' (undefined-variable)


"""