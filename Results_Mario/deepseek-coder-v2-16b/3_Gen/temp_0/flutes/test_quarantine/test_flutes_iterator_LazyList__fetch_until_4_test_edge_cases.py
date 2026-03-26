
import pytest
from flutes.iterator import LazyList

def test_edge_cases():
    my_empty_list = []
    lazy_empty_list = LazyList(my_empty_list)
    none_input = None
    lazy_none_list = LazyList(none_input)
    
    # Test empty list
    assert len(lazy_empty_list) == 0, "Expected length of lazy_empty_list to be 0"
    
    # Test None input
    with pytest.raises(TypeError):
        next(iter(lazy_none_list))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_4_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        my_empty_list = []
        lazy_empty_list = LazyList(my_empty_list)
        none_input = None
>       lazy_none_list = LazyList(none_input)

flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_4_test_edge_cases.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.iterator.LazyList object at 0x7f8dec96b510>, iterable = None

    def __init__(self, iterable: Iterable[T]):
>       self.iter = iter(iterable)
E       TypeError: 'NoneType' object is not iterable

flutes/flutes/iterator.py:254: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_LazyList__fetch_until_4_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.22s ===============================
"""