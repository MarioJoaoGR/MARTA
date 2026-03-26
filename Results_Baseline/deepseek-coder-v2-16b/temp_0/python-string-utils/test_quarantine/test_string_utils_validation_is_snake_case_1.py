
import re

# Test the function
def is_snake_case(input_string: str, separator: str = '_') -> bool:
    if isinstance(input_string, str) and len(input_string):
        pattern = fr'^[a-z]+({re.escape(separator)}[a-z]+)*$'
        return bool(re.match(pattern, input_string))
    return False

# Test the function with multiple test strings
test_strings = ["this_is_a_test", "ThisIsNotAllowed", "snake_case123"]
for test in test_strings:
    print(f"Testing '{test}': {is_snake_case(test)}")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.01s =============================

"""