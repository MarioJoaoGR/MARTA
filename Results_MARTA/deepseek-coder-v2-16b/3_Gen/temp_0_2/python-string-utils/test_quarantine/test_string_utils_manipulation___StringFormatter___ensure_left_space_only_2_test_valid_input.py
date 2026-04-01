
import pytest
from string_utils.manipulation import __StringFormatter

@pytest.fixture
def valid_formatter():
    return __StringFormatter("Hello, world!")

def test_valid_input(valid_formatter):
    formatted_string = valid_formatter._StringFormatter__ensure_left_space_only(None)
    assert formatted_string == " Hello, world!"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_left_space_only_2_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

valid_formatter = <string_utils.manipulation.__StringFormatter object at 0x105da1ea0>

    def test_valid_input(valid_formatter):
>       formatted_string = valid_formatter._StringFormatter__ensure_left_space_only(None)

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_left_space_only_2_test_valid_input.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <string_utils.manipulation.__StringFormatter object at 0x105da1ea0>
regex_match = None

    def __ensure_left_space_only(self, regex_match):
>       return ' ' + regex_match.group(1).strip()
E       AttributeError: 'NoneType' object has no attribute 'group'

python-string-utils/string_utils/manipulation.py:233: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_left_space_only_2_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""