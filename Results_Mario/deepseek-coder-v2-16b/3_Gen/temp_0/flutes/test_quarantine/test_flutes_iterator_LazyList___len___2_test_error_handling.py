
import pytest
from flutes.iterator import LazyList

def test_error_handling():
    lazy_list = LazyList([1, 2, 3, 4])
    
    # Access elements to ensure they are fetched lazily
    with pytest.raises(TypeError):
        assert next(iter(lazy_list)) == 1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___2_test_error_handling.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_error_handling ______________________________

    def test_error_handling():
        lazy_list = LazyList([1, 2, 3, 4])
    
        # Access elements to ensure they are fetched lazily
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___2_test_error_handling.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___2_test_error_handling.py::test_error_handling
============================== 1 failed in 0.07s ===============================

"""