
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
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_VariablesGenerator_generate_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________ test_generate_without_instantiation ______________________

    def test_generate_without_instantiation():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_VariablesGenerator_generate_0.py:6: Failed
_______________________ test_generate_with_instantiation _______________________

    def test_generate_with_instantiation():
        generator = VariablesGenerator()
>       assert generator.generate("var") == '_py_backwards_var_0'
E       AssertionError: assert '_py_backwards_var_1' == '_py_backwards_var_0'
E         
E         - _py_backwards_var_0
E         ?                   ^
E         + _py_backwards_var_1
E         ?                   ^

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_VariablesGenerator_generate_0.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_VariablesGenerator_generate_0.py::test_generate_without_instantiation
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_utils_helpers_VariablesGenerator_generate_0.py::test_generate_with_instantiation
============================== 2 failed in 0.06s ===============================
"""