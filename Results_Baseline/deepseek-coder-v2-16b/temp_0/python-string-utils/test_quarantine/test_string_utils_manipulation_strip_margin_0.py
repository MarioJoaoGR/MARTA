
# Module: string_utils.manipulation
# test_string_utils_manipulation.py
from string_utils.manipulation import strip_margin
import pytest

class InvalidInputError(Exception):
    pass

def test_strip_margin_with_indentation():
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
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

python-string-utils/Test4DT_tests/test_string_utils_manipulation_strip_margin_0.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
______________________ test_strip_margin_with_indentation ______________________

    def test_strip_margin_with_indentation():
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

python-string-utils/Test4DT_tests/test_string_utils_manipulation_strip_margin_0.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_strip_margin_0.py::test_strip_margin_with_indentation
========================= 1 failed, 1 passed in 0.02s ==========================

"""