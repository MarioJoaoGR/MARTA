
import pytest
from flutes.iterator import scanl
import operator

def test_valid_inputs():
    # Test with a list of integers and an initial value
    result = list(scanl(operator.add, [1, 2, 3, 4], 0))
    assert result == [0, 1, 3, 6, 10]
    
    # Test with a list of strings without an initial value
    result = list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd']))
    assert result == ['a', 'ba', 'cba', 'dcba']
    
    # Test with a list of floats and no initial value
    result = list(scanl(operator.mul, [1.0, 2.0, 3.0, 4.0]))
    assert result == [1.0, 2.0, 6.0, 24.0]
    
    # Test with an empty iterable and no initial value
    result = list(scanl(operator.add, []))
    pytest.raises(StopIteration)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_scanl_4_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

func = <built-in function add>
iterable = <list_iterator object at 0x7f013b4f7250>, args = ()

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

    def test_valid_inputs():
        # Test with a list of integers and an initial value
        result = list(scanl(operator.add, [1, 2, 3, 4], 0))
        assert result == [0, 1, 3, 6, 10]
    
        # Test with a list of strings without an initial value
        result = list(scanl(lambda s, x: x + s, ['a', 'b', 'c', 'd']))
        assert result == ['a', 'ba', 'cba', 'dcba']
    
        # Test with a list of floats and no initial value
        result = list(scanl(operator.mul, [1.0, 2.0, 3.0, 4.0]))
        assert result == [1.0, 2.0, 6.0, 24.0]
    
        # Test with an empty iterable and no initial value
>       result = list(scanl(operator.add, []))
E       RuntimeError: generator raised StopIteration

flutes/Test4DT_tests/test_flutes_iterator_scanl_4_test_valid_inputs.py:20: RuntimeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanl_4_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.10s ===============================

"""