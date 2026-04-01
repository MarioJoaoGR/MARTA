
import pytest
from operator import add

def scanl(func, iterable, *args):
    r"""Computes the intermediate results of :py:func:`~functools.reduce`. Equivalent to Haskell's ``scanl``. For
    example:

    .. code:: python

        >>> list(scanl(operator.add, [1, 2, 3, 4], 0))
        [0, 1, 3, 6, 10]
        >>> list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd']))
        ['a', 'ba', 'cba', 'dcba']

    Learn more at `Learn You a Haskell: Higher Order Functions <http://learnyouahaskell.com/higher-order-functions>`_.

    :param func: The function to apply. This should be a binary function where the arguments are: the accumulator,
        and the current element.
    :param iterable: The list of elements to iteratively apply the function to.
    :param initial: The initial value for the accumulator. If not supplied, the first element in the list is used.
    :return: The intermediate results at each step.
    """
    iterable = iter(iterable)
    if len(args) == 1:
        acc = args[0]
    elif len(args) == 0:
        acc = next(iterable)
    else:
        raise ValueError("Too many arguments")
    yield acc
    for x in iterable:
        acc = func(acc, x)
        yield acc

def test_valid_case_without_initial():
    result = list(scanl(add, [1, 2, 3, 4]))
    assert result == [1, 3, 6, 10]
