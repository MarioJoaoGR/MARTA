
import pytest
from pysnooper.utils import get_repr_function



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_utils_get_repr_function_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_case_int ______________________________

    def test_valid_case_int():
        item = 42
        custom_repr = [(lambda x: isinstance(x, int), lambda obj: f"Custom repr of {type(obj).__name__}")]
    
        result = get_repr_function(item, custom_repr)
        assert callable(result)
>       assert result.__name__ == 'custom_repr'
E       AssertionError: assert '<lambda>' == 'custom_repr'
E         
E         - custom_repr
E         + <lambda>

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_utils_get_repr_function_0.py:11: AssertionError
_____________________________ test_valid_case_str ______________________________

    def test_valid_case_str():
        item = "hello"
        custom_repr = [
            (lambda x: isinstance(x, int), lambda obj: f"Custom repr of {type(obj).__name__}"),
            (lambda x: isinstance(x, str), lambda obj: f"String repr of {obj}"),
            (lambda x: isinstance(x, list), lambda obj: "List representation")
        ]
    
        result = get_repr_function(item, custom_repr)
>       assert callable(result) is False
E       assert True is False
E        +  where True = callable(<function test_valid_case_str.<locals>.<lambda> at 0x7f34fd553ac0>)

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_utils_get_repr_function_0.py:22: AssertionError
_______________________________ test_error_case ________________________________

    def test_error_case():
        item = 42
        custom_repr = []
    
        result = get_repr_function(item, custom_repr)
>       assert str(type(result)) == "<class 'str'>"
E       assert "<class 'buil...n_or_method'>" == "<class 'str'>"
E         
E         - <class 'str'>
E         + <class 'builtin_function_or_method'>

/opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_utils_get_repr_function_0.py:30: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_utils_get_repr_function_0.py::test_valid_case_int
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_utils_get_repr_function_0.py::test_valid_case_str
FAILED ../../../../../opt/marta/baselines/Results_MARTA/PySnooper/Test4DT_tests_deepseek-coder-v2_16b/test_pysnooper_utils_get_repr_function_0.py::test_error_case
============================== 3 failed in 0.06s ===============================
"""