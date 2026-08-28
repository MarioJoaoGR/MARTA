
import pytest
from functools import reduce
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

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_compose_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_compose_with_functions __________________________

    def test_compose_with_functions():
        def add_one(x): return x + 1
        def multiply_by_two(x): return x * 2
    
        result = compose(5, add_one, multiply_by_two)
>       assert result == 12
E       assert 11 == 12

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_compose_1.py:11: AssertionError
__________________________ test_compose_with_lambdas ___________________________

    def test_compose_with_lambdas():
        result = compose(5, lambda x: x + 1, lambda x: x * 2)
>       assert result == 12
E       assert 11 == 12

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_compose_1.py:15: AssertionError
_______________________ test_compose_multiple_functions ________________________

    def test_compose_multiple_functions():
        def add_five(x): return x + 5
        def subtract_three(x): return x - 3
    
>       result = compose(5, add_one, multiply_by_two, add_five, subtract_three)
E       NameError: name 'add_one' is not defined

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_compose_1.py:21: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_compose_1.py::test_compose_with_functions
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_compose_1.py::test_compose_with_lambdas
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_compose_1.py::test_compose_multiple_functions
============================== 3 failed in 0.25s ===============================
"""