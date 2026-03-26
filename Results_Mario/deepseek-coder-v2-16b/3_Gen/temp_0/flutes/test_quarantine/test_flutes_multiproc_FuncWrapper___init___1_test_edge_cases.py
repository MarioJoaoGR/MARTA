
import pytest
from flutes.multiproc import FuncWrapper

def example_function(a, b=None):
    return a + (b or 0)

@pytest.fixture
def wrapper():
    return FuncWrapper(example_function, args=(1,), kwds={'b': 2})

def test_edge_cases(wrapper):
    # Test with None as an argument
    assert wrapper.fn(None) == 1

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___init___1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

wrapper = <flutes.multiproc.FuncWrapper object at 0x7fce2c9aca50>

    def test_edge_cases(wrapper):
        # Test with None as an argument
>       assert wrapper.fn(None) == 1

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___init___1_test_edge_cases.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

a = None, b = None

    def example_function(a, b=None):
>       return a + (b or 0)
E       TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___init___1_test_edge_cases.py:6: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___init___1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.10s ===============================
"""