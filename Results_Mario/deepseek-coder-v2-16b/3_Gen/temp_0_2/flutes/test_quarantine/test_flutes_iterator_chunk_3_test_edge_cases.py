
import pytest
from flutes.iterator import chunk
from typing import Iterable, List, Iterator, TypeVar

T = TypeVar('T')

def test_edge_cases():
    # Test with None as iterable
    with pytest.raises(ValueError):
        list(chunk(3, None))

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

flutes/Test4DT_tests/test_flutes_iterator_chunk_3_test_edge_cases.py F   [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test with None as iterable
        with pytest.raises(ValueError):
>           list(chunk(3, None))

flutes/Test4DT_tests/test_flutes_iterator_chunk_3_test_edge_cases.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = 3, iterable = None

    def chunk(n: int, iterable: Iterable[T]) -> Iterator[List[T]]:
        r"""Split the iterable into chunks, with each chunk containing no more than ``n`` elements.
    
        .. code:: python
    
            >>> list(chunk(3, range(10)))
            [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
    
        :param n: The maximum number of elements in one chunk.
        :param iterable: The iterable.
        :return: An iterator over chunks.
        """
        if n <= 0:
            raise ValueError("`n` should be positive")
        group = []
>       for x in iterable:
E       TypeError: 'NoneType' object is not iterable

flutes/flutes/iterator.py:38: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_chunk_3_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.10s ===============================
"""