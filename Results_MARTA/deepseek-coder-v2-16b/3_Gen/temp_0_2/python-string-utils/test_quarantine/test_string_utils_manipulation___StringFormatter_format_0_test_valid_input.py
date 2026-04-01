
from string_utils.manipulation import __StringFormatter, InvalidInputError
import re

# Mocking the necessary functions and constants for testing
URLS_RE = re.compile(r"https?://[^\s]+")
EMAILS_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
PRETTIFY_RE = {
    'UPPERCASE_FIRST_LETTER': re.compile(r'^([a-z])', re.IGNORECASE),
    'DUPLICATES': re.compile(r'(.)\1+'),
    'RIGHT_SPACE': re.compile(r' ([^\s)]+)'),
    'LEFT_SPACE': re.compile(r'( [^ ])'),
    'SPACES_AROUND': re.compile(r'\b'),
    'SPACES_INSIDE': re.compile(r'([a-zA-Z]) ( [a-zA-Z])'),
    'UPPERCASE_AFTER_SIGN': re.compile(r'(?<=[,.]) ([a-z])', re.IGNORECASE),
    'SAXON_GENITIVE': re.compile(r'([a-zA-Z]+) (s|S)')
}

def test_valid_input():
    formatter = __StringFormatter("This is a test string with an email example@example.com.")
    expected_output = "This Is A Test String With An Email $1$ Example@example.com."
    assert formatter.format() == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        formatter = __StringFormatter("This is a test string with an email example@example.com.")
        expected_output = "This Is A Test String With An Email $1$ Example@example.com."
>       assert formatter.format() == expected_output
E       AssertionError: assert 'This is a te...@example.com.' == 'This Is A Te...@example.com.'
E         
E         - This Is A Test String With An Email $1$ Example@example.com.
E         ?      ^  ^^^    ^      ^    ^  ^     ^^^^^
E         + This is a test string with an email example@example.com.
E         ?      ^  ^^^    ^      ^    ^  ^     ^

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_valid_input.py:22: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter_format_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""