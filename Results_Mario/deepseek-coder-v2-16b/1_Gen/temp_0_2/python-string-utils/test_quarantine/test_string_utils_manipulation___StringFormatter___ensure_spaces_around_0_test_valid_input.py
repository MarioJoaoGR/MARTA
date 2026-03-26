
import re
from string_utils.manipulation import is_string, InvalidInputError

class __StringFormatter:
    def __init__(self, input_string):
        if not is_string(input_string):
            raise InvalidInputError(f"Expected a string but got {type(input_string).__name__}")
        self.input_string = input_string

    def format(self):
        def __ensure_spaces_around(self, regex_match):
            return ' ' + regex_match.group(1).strip() + ' '
        
        formatted_string = re.sub(r'(?<!\s)(\w+)(?!\s)', lambda m: __ensure_spaces_around(self, m), self.input_string)
        return formatted_string.strip()

# Test function for valid input
def test_valid_input():
    formatter = __StringFormatter("Hello World")
    assert formatter.format() == "Hello World"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_spaces_around_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        formatter = __StringFormatter("Hello World")
>       assert formatter.format() == "Hello World"
E       AssertionError: assert 'Hell o W orld' == 'Hello World'
E         
E         - Hello World
E         + Hell o W orld
E         ?     +   +

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_spaces_around_0_test_valid_input.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_spaces_around_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""