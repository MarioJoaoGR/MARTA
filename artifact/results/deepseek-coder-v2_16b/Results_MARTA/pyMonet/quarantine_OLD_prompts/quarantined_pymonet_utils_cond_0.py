
import pytest
from pymonet.utils import cond



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_cond_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________________ test_cond_with_none ______________________________

    def test_cond_with_none():
        def is_even(n):
            return n % 2 == 0
    
        def double(n):
            return n * 2
    
        cond_func = cond([
            (is_even, double),
            (lambda n: n > 5, lambda n: n * 3)
        ])
    
>       assert cond_func(None) is None

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_cond_0.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/pyMonet/pymonet/utils.py:134: in result
    if condition_function(*args):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

n = None

    def is_even(n):
>       return n % 2 == 0
E       TypeError: unsupported operand type(s) for %: 'NoneType' and 'int'

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_cond_0.py:7: TypeError
______________________ test_cond_with_multiple_conditions ______________________

    def test_cond_with_multiple_conditions():
        def is_positive(n):
            return n > 0
    
        def square(n):
            return n * n
    
        cond_func = cond([
>           (is_even, double),
            (is_positive, square),
            (lambda n: n < -10, lambda n: -n)
        ])
E       NameError: name 'is_even' is not defined

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_cond_0.py:27: NameError
_______________________ test_cond_with_multiple_actions ________________________

    def test_cond_with_multiple_actions():
        def is_multiple_of_three(n):
            return n % 3 == 0
    
        def triple(n):
            return n * 3
    
        cond_func = cond([
>           (is_even, double),
            (is_multiple_of_three, triple),
            (lambda n: n > 10, lambda n: n + 5)
        ])
E       NameError: name 'is_even' is not defined

/opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_cond_0.py:44: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_cond_0.py::test_cond_with_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_cond_0.py::test_cond_with_multiple_conditions
FAILED ../../../../../opt/marta/baselines/Results_MARTA/pyMonet/Test4DT_tests_deepseek-coder-v2_16b/test_pymonet_utils_cond_0.py::test_cond_with_multiple_actions
============================== 3 failed in 0.08s ===============================
"""