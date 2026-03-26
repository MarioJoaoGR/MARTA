
import pytest
from flutes.iterator import scanl
import operator

@pytest.mark.parametrize("func, iterable", [
    (operator.add, None),  # func is not callable, iterable is None
    (operator.mul, "not_iterable"),  # func is callable, iterable is a string
    (lambda x: x, []),  # func is a lambda, iterable is an empty list
])
def test_invalid_inputs(func, iterable):
    with pytest.raises(TypeError):
        list(scanl(func, iterable))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_iterator_scanl_3_test_invalid_inputs.py . [ 33%]
.F                                                                       [100%]

=================================== FAILURES ===================================
___________________ test_invalid_inputs[<lambda>-iterable2] ____________________

func = <function <lambda> at 0x7f0e9f3e67a0>
iterable = <list_iterator object at 0x7f0e9f4e9ae0>, args = ()

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

func = <function <lambda> at 0x7f0e9f3e67a0>, iterable = []

    @pytest.mark.parametrize("func, iterable", [
        (operator.add, None),  # func is not callable, iterable is None
        (operator.mul, "not_iterable"),  # func is callable, iterable is a string
        (lambda x: x, []),  # func is a lambda, iterable is an empty list
    ])
    def test_invalid_inputs(func, iterable):
        with pytest.raises(TypeError):
>           list(scanl(func, iterable))
E           RuntimeError: generator raised StopIteration

flutes/Test4DT_tests/test_flutes_iterator_scanl_3_test_invalid_inputs.py:13: RuntimeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanl_3_test_invalid_inputs.py::test_invalid_inputs[<lambda>-iterable2]
========================= 1 failed, 2 passed in 0.10s ==========================

"""