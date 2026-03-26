
import re
from typing import Any, Optional, List

# Assuming URL_RE is a pre-defined regex for url validation
URL_RE = re.compile(r'^(http|https|ftp)://[^\s/$.?#].[^\s]*$')

def is_full_string(input_string: str) -> bool:
    return isinstance(input_string, str) and len(input_string.strip()) > 0

def is_url(input_string: Any, allowed_schemes: Optional[List[str]] = None) -> bool:
    if not is_full_string(input_string):
        return False

    valid = URL_RE.match(input_string) is not None

    if allowed_schemes:
        return valid and any([input_string.startswith(s) for s in allowed_schemes])

    return valid

def test_invalid_url():
    # Test cases for invalid URLs
    assert not is_url('http://')  # Invalid URL due to missing domain part
    assert not is_url('https://example')  # Invalid URL due to missing domain part
    assert not is_url('ftp://')  # Invalid URL due to missing domain part
    assert not is_url('http://.com')  # Invalid URL, no subdomain specified
    assert not is_url('https://mysite..com')  # Invalid URL, double dot in the domain part

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_url_8_test_invalid_url.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_invalid_url _______________________________

    def test_invalid_url():
        # Test cases for invalid URLs
        assert not is_url('http://')  # Invalid URL due to missing domain part
>       assert not is_url('https://example')  # Invalid URL due to missing domain part
E       AssertionError: assert not True
E        +  where True = is_url('https://example')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_url_8_test_invalid_url.py:25: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_url_8_test_invalid_url.py::test_invalid_url
============================== 1 failed in 0.03s ===============================
"""