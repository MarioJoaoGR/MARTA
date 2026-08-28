
import pytest
from apimd.parser import _type_name



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser__type_name_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
___________________ test_valid_case_with_user_defined_class ____________________

    def test_valid_case_with_user_defined_class():
        class MyClass: pass
        my_obj = MyClass()
        type_name = _type_name(my_obj)
>       assert type_name == 'MyClass'
E       AssertionError: assert 'test_valid_c...cals>.MyClass' == 'MyClass'
E         
E         - MyClass
E         + test_valid_case_with_user_defined_class.<locals>.MyClass

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser__type_name_0.py:9: AssertionError
___________________________ test_edge_case_with_none ___________________________

    def test_edge_case_with_none():
        obj = None
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser__type_name_0.py:13: Failed
______________________ test_error_case_with_invalid_input ______________________

    def test_error_case_with_invalid_input():
        invalid_input = 'string'
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser__type_name_0.py:18: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser__type_name_0.py::test_valid_case_with_user_defined_class
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser__type_name_0.py::test_edge_case_with_none
FAILED ../../../../../opt/marta/baselines/Results_MARTA/apimd/Test4DT_tests_deepseek-coder-v2_16b/test_apimd_parser__type_name_0.py::test_error_case_with_invalid_input
============================== 3 failed in 0.06s ===============================
"""