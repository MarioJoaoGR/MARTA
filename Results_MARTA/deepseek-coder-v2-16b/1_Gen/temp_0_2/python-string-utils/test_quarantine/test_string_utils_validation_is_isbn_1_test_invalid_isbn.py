
import re
from string_utils.validation import is_isbn

def test_invalid_isbn():
    # Test cases for invalid ISBN numbers
    invalid_isbns = [
        '978031249858',          # Too short (should be 13 digits)
        '97803124985800',        # Too long (should be 13 digits)
        '978-0-312-49858-00',    # Invalid checksum for ISBN-13
        '97803124985801',        # Invalid checksum for ISBN-13
        '150671521',             # Too short (should be 10 digits)
        '15067152144',           # Too long (should be 10 digits)
        '150671521-4',           # Invalid checksum for ISBN-10
        '978-0-312-49858-01',    # Invalid checksum for ISBN-13
        '978 0 312 49858 0',     # Contains spaces (invalid)
        '978-0-312-49858-0 abc', # Contains invalid characters
    ]
    
    for isbn in invalid_isbns:
        assert not is_isbn(isbn), f"{isbn} should be considered as an invalid ISBN"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_1_test_invalid_isbn.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_isbn _______________________________

    def test_invalid_isbn():
        # Test cases for invalid ISBN numbers
        invalid_isbns = [
            '978031249858',          # Too short (should be 13 digits)
            '97803124985800',        # Too long (should be 13 digits)
            '978-0-312-49858-00',    # Invalid checksum for ISBN-13
            '97803124985801',        # Invalid checksum for ISBN-13
            '150671521',             # Too short (should be 10 digits)
            '15067152144',           # Too long (should be 10 digits)
            '150671521-4',           # Invalid checksum for ISBN-10
            '978-0-312-49858-01',    # Invalid checksum for ISBN-13
            '978 0 312 49858 0',     # Contains spaces (invalid)
            '978-0-312-49858-0 abc', # Contains invalid characters
        ]
    
        for isbn in invalid_isbns:
>           assert not is_isbn(isbn), f"{isbn} should be considered as an invalid ISBN"
E           AssertionError: 150671521-4 should be considered as an invalid ISBN
E           assert not True
E            +  where True = is_isbn('150671521-4')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_1_test_invalid_isbn.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_1_test_invalid_isbn.py::test_invalid_isbn
============================== 1 failed in 0.04s ===============================
"""