
import pytest
from functools import reduce
from operator import add

def scanl(func, iterable, *args):
    result = []
    accumulator = args[0] if args else None
    for element in iterable:
        accumulator = func(accumulator, element)
        result.append(accumulator)
    return result

def scanr(func, iterable, *args):
    r"""Computes the intermediate results of :py:func:`~functools.reduce` applied in reverse. Equivalent to Haskell's
    ``scanr``. For example:

    .. code:: python

        >>> scanr(operator.add, [1, 2, 3, 4], 0)
        [10, 9, 7, 4, 0]
        >>> scanr(lambda s, x: x + s, ['a', 'b', 'c', 'd'])
        ['abcd', 'bcd', 'cd', 'd']

    Learn more at `Learn You a Haskell: Higher Order Functions <http://learnyouahaskell.com/higher-order-functions>`_.

    :param func: The function to apply. This should be a binary function where the arguments are: the accumulator,
        and the current element.
    :param iterable: The list of elements to iteratively apply the function to.
    :param initial: The initial value for the accumulator. If not supplied, the first element in the list is used.
    :return: The intermediate results at each step, starting from the end.
    """
    return list(scanl(func, reversed(iterable), *args))[::-1]

def test_invalid_input():
    with pytest.raises(TypeError):
        scanr("not a function", [1, 2, 3])
    
    with pytest.raises(ValueError):
        scanr(add, [], initial=0)
    
    with pytest.raises(IndexError):
        scanr(add, [])

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_iterator_scanr_2_test_invalid_input
flutes/Test4DT_tests/test_flutes_iterator_scanr_2_test_invalid_input.py:40:8: E1123: Unexpected keyword argument 'initial' in function call (unexpected-keyword-arg)


"""