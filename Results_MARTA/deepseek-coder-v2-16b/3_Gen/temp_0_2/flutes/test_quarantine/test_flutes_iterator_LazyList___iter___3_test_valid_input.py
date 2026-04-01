
import pytest
from flutes.iterator import LazyList

def test_valid_input():
    lazy_list = LazyList([1, 2, 3, 4])
    iterator = iter(lazy_list)
    
    assert next(iterator) == 1
    assert next(iterator) == 2
    assert next(iterator) == 3
    with pytest.raises(StopIteration):
        next(iterator)

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

flutes/Test4DT_tests/test_flutes_iterator_LazyList___iter___3_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        lazy_list = LazyList([1, 2, 3, 4])
        iterator = iter(lazy_list)
    
        assert next(iterator) == 1
        assert next(iterator) == 2
        assert next(iterator) == 3
>       with pytest.raises(StopIteration):
E       Failed: DID NOT RAISE <class 'StopIteration'>

flutes/Test4DT_tests/test_flutes_iterator_LazyList___iter___3_test_valid_input.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_LazyList___iter___3_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""