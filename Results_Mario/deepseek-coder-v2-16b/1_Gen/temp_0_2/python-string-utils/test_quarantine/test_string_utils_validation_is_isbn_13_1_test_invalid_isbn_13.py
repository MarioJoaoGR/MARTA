
import re
from string_utils.validation import is_isbn_13

def test_invalid_isbn_13():
    # Test cases for invalid ISBN-13 numbers
    invalid_isbn_cases = [
        "978031249858",  # Too short
        "97803124985800",  # Too long
        "978031249858a",  # Contains a letter
        "978-0312-4985-80",  # Valid format but incorrect checksum
        "9780312498580",  # Correct format but invalid checksum
    ]
    
    for isbn in invalid_isbn_cases:
        assert not is_isbn_13(isbn), f"Expected {isbn} to be invalid, but it was recognized as valid."

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
        # Test cases for invalid ISBN-13 numbers
        invalid_isbn_cases = [
            "978031249858",  # Too short
            "97803124985800",  # Too long
            "978031249858a",  # Contains a letter
            "978-0312-4985-80",  # Valid format but incorrect checksum
            "9780312498580",  # Correct format but invalid checksum
        ]
    
        for isbn in invalid_isbn_cases:
>           assert not is_isbn_13(isbn), f"Expected {isbn} to be invalid, but it was recognized as valid."
E           AssertionError: Expected 978-0312-4985-80 to be invalid, but it was recognized as valid.
E           assert not True
E            +  where True = is_isbn_13('978-0312-4985-80')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_13_1_test_invalid_isbn_13.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_13_1_test_invalid_isbn_13.py::test_invalid_isbn_13
============================== 1 failed in 0.08s ===============================
"""