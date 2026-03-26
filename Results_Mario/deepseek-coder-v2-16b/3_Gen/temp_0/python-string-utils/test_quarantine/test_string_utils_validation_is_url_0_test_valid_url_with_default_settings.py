
import re
from typing import Optional, List, Any

# Assuming URL_RE is defined somewhere in string_utils.validation module
URL_RE = re.compile(r'^https?://[^\s]+$')

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string) > 0

def is_url(input_string: Any, allowed_schemes: Optional[List[str]] = None) -> bool:
    """
    Check if a string is a valid url.

    *Examples:*

    >>> is_url('http://www.mysite.com') # returns true
    >>> is_url('https://mysite.com') # returns true
    >>> is_url('.mysite.com') # returns false

    :param input_string: String to check.
    :type input_string: str
    :param allowed_schemes: List of valid schemes ('http', 'https', 'ftp'...). Default to None (any scheme is valid).
    :type allowed_schemes: Optional[List[str]]
    :return: True if url, false otherwise
    """
    if not is_full_string(input_string):
        return False

    valid = URL_RE.match(input_string) is not None

    if allowed_schemes:
        return valid and any([input_string.startswith(s) for s in allowed_schemes])

    return valid

import pytest

@pytest.mark.parametrize("input_string, expected", [
    ('http://www.mysite.com', True),
    ('https://mysite.com', True),
    ('.mysite.com', False),
    ('ftp://example.com', True)  # Test with allowed scheme
])
def test_valid_url_with_default_settings(input_string, expected):
    assert is_url(input_string) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_url_0_test_valid_url_with_default_settings.py . [ 25%]
..F                                                                      [100%]

=================================== FAILURES ===================================
_________ test_valid_url_with_default_settings[ftp://example.com-True] _________

input_string = 'ftp://example.com', expected = True

    @pytest.mark.parametrize("input_string, expected", [
        ('http://www.mysite.com', True),
        ('https://mysite.com', True),
        ('.mysite.com', False),
        ('ftp://example.com', True)  # Test with allowed scheme
    ])
    def test_valid_url_with_default_settings(input_string, expected):
>       assert is_url(input_string) == expected
E       AssertionError: assert False == True
E        +  where False = is_url('ftp://example.com')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_url_0_test_valid_url_with_default_settings.py:46: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_url_0_test_valid_url_with_default_settings.py::test_valid_url_with_default_settings[ftp:/example.com-True]
========================= 1 failed, 3 passed in 0.02s ==========================
"""