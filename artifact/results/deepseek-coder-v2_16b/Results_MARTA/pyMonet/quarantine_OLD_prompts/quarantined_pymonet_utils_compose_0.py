
import pytest
from pymonet.utils import compose



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_compose_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_compose_basic ______________________________

    def test_compose_basic():
        def add_one(x): return x + 1
        def multiply_by_two(x): return x * 2
    
        result = compose(5, add_one, multiply_by_two)
>       assert result == 12
E       assert 11 == 12

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_compose_0.py:10: AssertionError
_____________________________ test_compose_lambda ______________________________

    def test_compose_lambda():
        result = compose(5, lambda x: x + 1, lambda x: x * 2)
>       assert result == 12
E       assert 11 == 12

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_compose_0.py:14: AssertionError
_______________________ test_compose_multiple_functions ________________________

    def test_compose_multiple_functions():
        def add_five(x): return x + 5
        def subtract_three(x): return x - 3
    
        result = compose(5, lambda x: x + 1, lambda x: x * 2, lambda x: x + 5, lambda x: x - 3)
>       assert result == 14
E       assert 15 == 14

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_compose_0.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_compose_0.py::test_compose_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_compose_0.py::test_compose_lambda
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_compose_0.py::test_compose_multiple_functions
============================== 3 failed in 0.06s ===============================
"""