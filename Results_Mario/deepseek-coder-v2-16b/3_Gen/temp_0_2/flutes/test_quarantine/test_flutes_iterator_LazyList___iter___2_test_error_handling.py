
import pytest
from flutes.iterator import LazyList

def test_error_handling():
    # Create a LazyList instance with an iterable that will raise an error when iterated over
    class ErrorIterable:
        def __iter__(self):
            raise ValueError("Test error")
    
    lazy_list = LazyList(ErrorIterable())
    
    # Use pytest to check if the iterator raises the expected exception
    with pytest.raises(ValueError) as excinfo:
        for _ in lazy_list:
            pass
    
    assert str(excinfo.value) == "Test error"

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

flutes/Test4DT_tests/test_flutes_iterator_LazyList___iter___2_test_error_handling.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_error_handling ______________________________

    def test_error_handling():
        # Create a LazyList instance with an iterable that will raise an error when iterated over
        class ErrorIterable:
            def __iter__(self):
                raise ValueError("Test error")
    
>       lazy_list = LazyList(ErrorIterable())

flutes/Test4DT_tests/test_flutes_iterator_LazyList___iter___2_test_error_handling.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/iterator.py:254: in __init__
    self.iter = iter(iterable)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Test4DT_tests.test_flutes_iterator_LazyList___iter___2_test_error_handling.test_error_handling.<locals>.ErrorIterable object at 0x7fef73c07250>

    def __iter__(self):
>       raise ValueError("Test error")
E       ValueError: Test error

flutes/Test4DT_tests/test_flutes_iterator_LazyList___iter___2_test_error_handling.py:9: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_LazyList___iter___2_test_error_handling.py::test_error_handling
============================== 1 failed in 0.09s ===============================
"""