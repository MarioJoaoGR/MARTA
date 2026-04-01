
from string_utils.validation import is_isbn_13

def test_invalid_isbn_13():
    # Valid ISBN-13 without hyphens
    assert not is_isbn_13('9780312498580')  # True, but we expect False here because it's valid and should pass normalization

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_13_1_test_invalid_isbn_13.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_isbn_13 _____________________________

    def test_invalid_isbn_13():
        # Valid ISBN-13 without hyphens
>       assert not is_isbn_13('9780312498580')  # True, but we expect False here because it's valid and should pass normalization
E       AssertionError: assert not True
E        +  where True = is_isbn_13('9780312498580')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_13_1_test_invalid_isbn_13.py:6: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_13_1_test_invalid_isbn_13.py::test_invalid_isbn_13
============================== 1 failed in 0.03s ===============================
"""