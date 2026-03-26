
import pytest
from typing import Iterable, List, Iterator, TypeVar
from flutes.iterator import chunk

T = TypeVar('T')

def test_chunk_invalid_n():
    with pytest.raises(ValueError):
        list(chunk(-1, range(10)))

def test_chunk_zero_n():
    with pytest.raises(ValueError):
        list(chunk(0, range(10)))

def test_chunk_string_as_iterable():
    result = list(chunk(3, "hello"))
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_iterator_chunk_1.py ..F                 [100%]

=================================== FAILURES ===================================
________________________ test_chunk_string_as_iterable _________________________

    def test_chunk_string_as_iterable():
        result = list(chunk(3, "hello"))
>       assert result == ["hel", "lo"]  # Corrected assertion to match the chunk size
E       AssertionError: assert [['h', 'e', 'l'], ['l', 'o']] == ['hel', 'lo']
E         
E         At index 0 diff: ['h', 'e', 'l'] != 'hel'
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_chunk_1.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_chunk_1.py::test_chunk_string_as_iterable
========================= 1 failed, 2 passed in 0.09s ==========================
"""