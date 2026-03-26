
import pytest
from pymonet.utils import curry

def test_edge_cases():
    # Test None input
    with pytest.raises(TypeError):
        curried_none = curry(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pyMonet
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pyMonet/Test4DT_tests/test_pymonet_utils_curry_1_test_edge_cases.py F    [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        # Test None input
        with pytest.raises(TypeError):
>           curried_none = curry(None)

pyMonet/Test4DT_tests/test_pymonet_utils_curry_1_test_edge_cases.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

x = None, args_count = None

    def curry(x, args_count=None):
        """
        In mathematics and computer science, currying is the technique of translating the evaluation of a function.
        It that takes multiple arguments (or a tuple of arguments) into evaluating a sequence of functions.
        each with a single argument.
        """
        if args_count is None:
>           args_count = x.__code__.co_argcount
E           AttributeError: 'NoneType' object has no attribute '__code__'

pyMonet/pymonet/utils.py:16: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pyMonet/Test4DT_tests/test_pymonet_utils_curry_1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.08s ===============================
"""