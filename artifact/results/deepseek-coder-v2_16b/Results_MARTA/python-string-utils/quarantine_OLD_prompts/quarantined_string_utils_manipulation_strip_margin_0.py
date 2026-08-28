
import pytest
from string_utils.manipulation import strip_margin



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_strip_margin_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        input_string = '''
            line 1
            line 2
            line 3
        '''
        expected_output = '''
        line 1
        line 2
        line 3
        '''
>       assert strip_margin(input_string) == expected_output.strip()
E       AssertionError: assert '\nline 1\nline 2\nline 3\n' == 'line 1\n    ...2\n    line 3'
E         
E         + 
E           line 1
E         -     line 2
E         ? ----
E         + line 2
E         -     line 3
E         + line 3

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_strip_margin_0.py:16: AssertionError
_______________________ test_valid_different_indentation _______________________

    def test_valid_different_indentation():
        input_string = '''
        	line 1
            line 2
            line 3
        '''
        expected_output = '''
        line 1
        line 2
        line 3
        '''
>       assert strip_margin(input_string) == expected_output.strip()
E       AssertionError: assert '\nline 1\nline 2\nline 3\n' == 'line 1\n    ...2\n    line 3'
E         
E         + 
E           line 1
E         -     line 2
E         ? ----
E         + line 2
E         -     line 3
E         + line 3

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_strip_margin_0.py:29: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
>       with pytest.raises(InvalidInputError):
E       NameError: name 'InvalidInputError' is not defined

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_strip_margin_0.py:32: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_strip_margin_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_strip_margin_0.py::test_valid_different_indentation
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_strip_margin_0.py::test_invalid_input
============================== 3 failed in 0.06s ===============================
"""