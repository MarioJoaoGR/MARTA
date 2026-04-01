
from string_utils.validation import is_isbn_10

def test_valid_isbn_10():
    # Test cases for valid ISBN-10 numbers with and without hyphens
    valid_isbns = [
        '1506715214',  # Without hyphens
        '150-6715214', # With hyphens
        '9780470059028', # Another valid ISBN-10 without hyphens
        '978-0-470-05902-8' # Valid ISBN-10 with hyphens
    ]
    
    for isbn in valid_isbns:
        assert is_isbn_10(isbn) == True, f"{isbn} should be a valid ISBN-10"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_10_0_test_valid_isbn_10.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_isbn_10 ______________________________

    def test_valid_isbn_10():
        # Test cases for valid ISBN-10 numbers with and without hyphens
        valid_isbns = [
            '1506715214',  # Without hyphens
            '150-6715214', # With hyphens
            '9780470059028', # Another valid ISBN-10 without hyphens
            '978-0-470-05902-8' # Valid ISBN-10 with hyphens
        ]
    
        for isbn in valid_isbns:
>           assert is_isbn_10(isbn) == True, f"{isbn} should be a valid ISBN-10"
E           AssertionError: 9780470059028 should be a valid ISBN-10
E           assert False == True
E            +  where False = is_isbn_10('9780470059028')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_10_0_test_valid_isbn_10.py:14: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_10_0_test_valid_isbn_10.py::test_valid_isbn_10
============================== 1 failed in 0.02s ===============================
"""