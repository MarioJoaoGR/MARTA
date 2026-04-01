
import pytest
from string_utils.manipulation import __StringFormatter

# Mocking URLS_RE, EMAILS_RE, PRETTIFY_RE for testing purposes
URLS_RE = None
EMAILS_RE = None
PRETTIFY_RE = {
    'UPPERCASE_FIRST_LETTER': lambda x: x.sub(lambda m: m.group().capitalize(), x),
    'DUPLICATES': lambda x: x.sub(lambda m: m.group().replace('a', ''), x),
    'RIGHT_SPACE': lambda x: x.sub(lambda m: m.group() + ' ', x),
    'LEFT_SPACE': lambda x: x.sub(lambda m: ' ' + m.group(), x),
    'SPACES_AROUND': lambda x: x.sub(lambda m: ' ' + m.group() + ' ', x),
    'SPACES_INSIDE': lambda x: x.sub(lambda m: m.group().replace('a', 'b'), x),
    'UPPERCASE_AFTER_SIGN': lambda x: x.sub(lambda m: m.group().upper(), x),
    'SAXON_GENITIVE': lambda x: x.sub(lambda m: m.group().replace('s', 'z'), x)
}

@pytest.fixture
def string_formatter():
    return __StringFormatter("initial input string")

def test_format_string(string_formatter):
    # Test the format method of __StringFormatter class
    assert string_formatter.format() == "Initial Input String"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_2_test_edge_case.py F [100%]

=================================== FAILURES ===================================
______________________________ test_format_string ______________________________

string_formatter = <string_utils.manipulation.__StringFormatter object at 0x106c27b20>

    def test_format_string(string_formatter):
        # Test the format method of __StringFormatter class
>       assert string_formatter.format() == "Initial Input String"
E       AssertionError: assert 'Initial input string' == 'Initial Input String'
E         
E         - Initial Input String
E         ?         ^     ^
E         + Initial input string
E         ?         ^     ^

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_2_test_edge_case.py:25: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_2_test_edge_case.py::test_format_string
============================== 1 failed in 0.03s ===============================
"""