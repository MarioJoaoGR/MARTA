
import pytest
from flutes.iterator import LazyList

def test_valid_inputs():
    lazy_list = LazyList([1, 2, 3, 4])
    
    # Check initial length before any elements are accessed
    with pytest.raises(TypeError):
        len(lazy_list)
    
    # Access the first element
    assert next(lazy_list) == 1

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

flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        lazy_list = LazyList([1, 2, 3, 4])
    
        # Check initial length before any elements are accessed
        with pytest.raises(TypeError):
            len(lazy_list)
    
        # Access the first element
>       assert next(lazy_list) == 1
E       TypeError: 'LazyList' object is not an iterator

flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___1_test_valid_inputs.py:13: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_LazyList___len___1_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.10s ===============================
"""