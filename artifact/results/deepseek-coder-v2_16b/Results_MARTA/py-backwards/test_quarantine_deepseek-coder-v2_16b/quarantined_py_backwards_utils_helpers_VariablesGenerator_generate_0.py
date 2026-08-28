
import pytest
from py_backwards.utils.helpers import VariablesGenerator



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_VariablesGenerator_generate_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        generator = VariablesGenerator()
        assert generator.generate("var") == '_py_backwards_var_0'
        assert generator.generate("var") == '_py_backwards_var_1'
>       assert generator.generate("another_var") == '_py_backwards_another_var_0'
E       AssertionError: assert '_py_backwards_another_var_2' == '_py_backwards_another_var_0'
E         
E         - _py_backwards_another_var_0
E         ?                           ^
E         + _py_backwards_another_var_2
E         ?                           ^

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_VariablesGenerator_generate_0.py:9: AssertionError
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        generator = VariablesGenerator()
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_VariablesGenerator_generate_0.py:13: Failed
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        generator = VariablesGenerator()
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_VariablesGenerator_generate_0.py:18: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_VariablesGenerator_generate_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_VariablesGenerator_generate_0.py::test_edge_case_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_VariablesGenerator_generate_0.py::test_invalid_input
============================== 3 failed in 0.06s ===============================
"""