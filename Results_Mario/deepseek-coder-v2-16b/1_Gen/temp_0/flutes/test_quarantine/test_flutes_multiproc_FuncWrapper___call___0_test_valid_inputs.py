
import pytest
from flutes.multiproc import FuncWrapper

def example_function(a, b=None):
    return a + (b or 0)

@pytest.fixture
def wrapper():
    return FuncWrapper(example_function, args=(1,), kwds={'b': 2})

def test_valid_inputs(wrapper):
    assert wrapper.fn() == 3

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

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

wrapper = <flutes.multiproc.FuncWrapper object at 0x7f65ca7bf090>

    def test_valid_inputs(wrapper):
>       assert wrapper.fn() == 3
E       TypeError: example_function() missing 1 required positional argument: 'a'

flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___0_test_valid_inputs.py:13: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_FuncWrapper___call___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.08s ===============================
"""