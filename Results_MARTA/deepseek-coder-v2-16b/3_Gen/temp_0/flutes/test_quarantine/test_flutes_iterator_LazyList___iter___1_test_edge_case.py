
import pytest
from flutes.iterator import LazyList

def test_edge_case():
    lazy_list_none = LazyList(None)
    with pytest.raises(TypeError):
        iter(lazy_list_none)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_LazyList___iter___1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
>       lazy_list_none = LazyList(None)

flutes/Test4DT_tests/test_flutes_iterator_LazyList___iter___1_test_edge_case.py:6: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.iterator.LazyList object at 0x7f0867b8b9d0>, iterable = None

    def __init__(self, iterable: Iterable[T]):
>       self.iter = iter(iterable)
E       TypeError: 'NoneType' object is not iterable

flutes/flutes/iterator.py:254: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_LazyList___iter___1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.09s ===============================

"""