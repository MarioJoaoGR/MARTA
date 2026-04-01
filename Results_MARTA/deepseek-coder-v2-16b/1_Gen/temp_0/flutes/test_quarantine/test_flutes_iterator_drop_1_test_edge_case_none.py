
import pytest
from flutes.iterator import drop

def test_edge_case_none():
    with pytest.raises(ValueError):
        result = list(drop(3, None))

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

flutes/Test4DT_tests/test_flutes_iterator_drop_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        with pytest.raises(ValueError):
>           result = list(drop(3, None))

flutes/Test4DT_tests/test_flutes_iterator_drop_1_test_edge_case_none.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 3, iterable = None

    def drop(n: int, iterable: Iterable[T]) -> Iterator[T]:
        r"""Drop the first :attr:`n` elements from an iterable, and return the rest as an iterator.
    
        .. code:: python
    
            >>> next(drop(5, range(1000000)))
            5
    
        :param n: The number of elements to drop.
        :param iterable: The iterable.
        :return: An iterator returning the remaining part of the iterable after the first :attr:`n` elements.
        """
        if n < 0:
            raise ValueError("`n` should be non-negative")
        try:
>           it = iter(iterable)
E           TypeError: 'NoneType' object is not iterable

flutes/flutes/iterator.py:84: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_drop_1_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.09s ===============================
"""