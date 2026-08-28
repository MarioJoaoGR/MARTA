
import pytest
from string_utils.manipulation import strip_margin

def is_string(obj):
    return isinstance(obj, str)

class InvalidInputError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Expected "str", received "{type(self.value).__name__}"'



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

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_strip_margin_0.py:26: AssertionError
_________________ test_valid_input_with_different_indentation __________________

    def test_valid_input_with_different_indentation():
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

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_strip_margin_0.py:39: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(InvalidInputError):
>           strip_margin(None)

/opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_strip_margin_0.py:43: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

input_string = None

    def strip_margin(input_string: str) -> str:
        """
        Removes tab indentation from multi line strings (inspired by analogous Scala function).
    
        *Example:*
    
        >>> strip_margin('''
        >>>                 line 1
        >>>                 line 2
        >>>                 line 3
        >>> ''')
        >>> # returns:
        >>> '''
        >>> line 1
        >>> line 2
        >>> line 3
        >>> '''
    
        :param input_string: String to format
        :type input_string: str
        :return: A string without left margins
        """
        if not is_string(input_string):
>           raise InvalidInputError(input_string)
E           string_utils.errors.InvalidInputError: Expected "str", received "NoneType"

/opt/marta/baselines/codamosa/replication/test-apps/python-string-utils/string_utils/manipulation.py:552: InvalidInputError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_strip_margin_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_strip_margin_0.py::test_valid_input_with_different_indentation
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-string-utils/Test4DT_tests_deepseek-coder-v2_16b/test_string_utils_manipulation_strip_margin_0.py::test_invalid_input
============================== 3 failed in 0.07s ===============================
"""