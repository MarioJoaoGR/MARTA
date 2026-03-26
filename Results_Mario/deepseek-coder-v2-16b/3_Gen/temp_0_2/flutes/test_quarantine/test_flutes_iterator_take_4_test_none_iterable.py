
import pytest
from flutes.iterator import take

def test_none_iterable():
    with pytest.raises(ValueError):
        list(take(5, None))

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

flutes/Test4DT_tests/test_flutes_iterator_take_4_test_none_iterable.py F [100%]

=================================== FAILURES ===================================
______________________________ test_none_iterable ______________________________

    def test_none_iterable():
        with pytest.raises(ValueError):
>           list(take(5, None))

flutes/Test4DT_tests/test_flutes_iterator_take_4_test_none_iterable.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 5, iterable = None

    def take(n: int, iterable: Iterable[T]) -> Iterator[T]:
        r"""Take the first :attr:`n` elements from an iterable.
    
        .. code:: python
    
            >>> list(take(5, range(1000000)))
            [0, 1, 2, 3, 4]
    
        :param n: The number of elements to take.
        :param iterable: The iterable.
        :return: An iterator returning the first :attr:`n` elements from the iterable.
        """
        if n < 0:
            raise ValueError("`n` should be non-negative")
        try:
>           it = iter(iterable)
E           TypeError: 'NoneType' object is not iterable

flutes/flutes/iterator.py:62: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_take_4_test_none_iterable.py::test_none_iterable
============================== 1 failed in 0.10s ===============================
"""