
from flutes.iterator import LazyList
import pytest

def test_none_input():
    lazy_list = LazyList(None)
    assert len(lazy_list) == 0

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

flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___0_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
>       lazy_list = LazyList(None)

flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___0_test_none_input.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.iterator.LazyList object at 0x7fd7c7244190>, iterable = None

    def __init__(self, iterable: Iterable[T]):
>       self.iter = iter(iterable)
E       TypeError: 'NoneType' object is not iterable

flutes/flutes/iterator.py:254: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___0_test_none_input.py::test_none_input
============================== 1 failed in 0.09s ===============================
"""