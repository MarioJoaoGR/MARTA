
import pytest
from unittest.mock import patch
from string_utils.manipulation import camel_case_to_snake, is_camel_case


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_camel_case_to_snake_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_valid_camel_case _____________________________

    def test_valid_camel_case():
        with patch('string_utils.manipulation.is_camel_case', return_value=True):
>           assert camel_case_to_snake('ThisIsACamelStringTest') == 'this_is_a_camel_case_string_test'
E           AssertionError: assert 'this_is_a_camel_string_test' == 'this_is_a_ca...e_string_test'
E             
E             - this_is_a_camel_case_string_test
E             ?                 -----
E             + this_is_a_camel_string_test

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_camel_case_to_snake_0.py:8: AssertionError
__________________________ test_non_camel_case_input ___________________________

    def test_non_camel_case_input():
        input_string = 'thisIsNotACamelStringTest'
>       assert camel_case_to_snake(input_string) == input_string
E       AssertionError: assert 'this_is_not_...l_string_test' == 'thisIsNotACamelStringTest'
E         
E         - thisIsNotACamelStringTest
E         + this_is_not_a_camel_string_test

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_camel_case_to_snake_0.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_camel_case_to_snake_0.py::test_valid_camel_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_camel_case_to_snake_0.py::test_non_camel_case_input
============================== 2 failed in 0.06s ===============================
"""