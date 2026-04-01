
import pytest
from flutes.iterator import scanl

def test_valid_input():
    # Test case 1: Summing up elements of a list
    result = list(scanl(lambda x, y: x + y, [1, 2, 3, 4]))
    assert result == [1, 3, 6, 10]
    
    # Test case 2: Multiplying elements of a list
    result = list(scanl(lambda x, y: x * y, [1, 2, 3, 4]))
    assert result == [1, 2, 6, 24]
    
    # Test case 3: Using scanl with a generator expression
    result = list(scanl(lambda x, y: x + y, (x for x in range(1, 5))))
    assert result == [1, 3, 6, 10]
    
    # Test case 4: Using scanl with an empty iterable
    result = list(scanl(lambda x, y: x + y, []))
    assert result == []

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_scanl_2_test_valid_input.py F  [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

func = <function test_valid_input.<locals>.<lambda> at 0x7ff87a8c93a0>
iterable = <list_iterator object at 0x7ff87a881f30>, args = ()

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
>           acc = next(iterable)
E           StopIteration

flutes/flutes/iterator.py:191: StopIteration

The above exception was the direct cause of the following exception:

    def test_valid_input():
        # Test case 1: Summing up elements of a list
        result = list(scanl(lambda x, y: x + y, [1, 2, 3, 4]))
        assert result == [1, 3, 6, 10]
    
        # Test case 2: Multiplying elements of a list
        result = list(scanl(lambda x, y: x * y, [1, 2, 3, 4]))
        assert result == [1, 2, 6, 24]
    
        # Test case 3: Using scanl with a generator expression
        result = list(scanl(lambda x, y: x + y, (x for x in range(1, 5))))
        assert result == [1, 3, 6, 10]
    
        # Test case 4: Using scanl with an empty iterable
>       result = list(scanl(lambda x, y: x + y, []))
E       RuntimeError: generator raised StopIteration

flutes/Test4DT_tests/test_flutes_iterator_scanl_2_test_valid_input.py:19: RuntimeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanl_2_test_valid_input.py::test_valid_input
============================== 1 failed in 0.15s ===============================
"""