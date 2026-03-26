
from flutes.iterator import scanl
import operator

def test_edge_case_empty_list():
    # Define a dummy binary function
    def add(x, y):
        return x + y
    
    # Test with an empty list
    result = list(scanl(add, []))
    assert result == [], f"Expected an empty list but got {result}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_scanl_1_test_edge_case_empty_list.py F [100%]

=================================== FAILURES ===================================
__________________________ test_edge_case_empty_list ___________________________

func = <function test_edge_case_empty_list.<locals>.add at 0x7fd184e3c220>
iterable = <list_iterator object at 0x7fd184be5c00>, args = ()

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

    def test_edge_case_empty_list():
        # Define a dummy binary function
        def add(x, y):
            return x + y
    
        # Test with an empty list
>       result = list(scanl(add, []))
E       RuntimeError: generator raised StopIteration

flutes/Test4DT_tests/test_flutes_iterator_scanl_1_test_edge_case_empty_list.py:11: RuntimeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanl_1_test_edge_case_empty_list.py::test_edge_case_empty_list
============================== 1 failed in 0.11s ===============================
"""