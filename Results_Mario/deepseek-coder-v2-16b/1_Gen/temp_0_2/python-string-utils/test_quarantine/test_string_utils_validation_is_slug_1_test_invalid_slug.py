
import re
from string_utils.validation import is_slug

def test_invalid_slug():
    # Test cases where input strings are not valid slugs
    assert not is_slug('My blog post title')  # Should return False as it contains uppercase letters and spaces
    assert not is_slug('This-is-a-test--string')  # Contains double separators which is invalid
    assert not is_slug('Invalid!Slug')  # Contains an exclamation mark which is not allowed in slugs
    assert not is_slug('1234567890')  # Only digits, no separator or lowercase letters

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_slug_1_test_invalid_slug.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_slug _______________________________

    def test_invalid_slug():
        # Test cases where input strings are not valid slugs
        assert not is_slug('My blog post title')  # Should return False as it contains uppercase letters and spaces
        assert not is_slug('This-is-a-test--string')  # Contains double separators which is invalid
        assert not is_slug('Invalid!Slug')  # Contains an exclamation mark which is not allowed in slugs
>       assert not is_slug('1234567890')  # Only digits, no separator or lowercase letters
E       AssertionError: assert not True
E        +  where True = is_slug('1234567890')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_slug_1_test_invalid_slug.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_slug_1_test_invalid_slug.py::test_invalid_slug
============================== 1 failed in 0.03s ===============================
"""