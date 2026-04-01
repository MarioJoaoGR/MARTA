
import pytest
from string_utils.validation import is_isbn_10

@pytest.mark.parametrize("input_string, expected", [
    ('150-6715214', False),  # Invalid ISBN-10 with hyphens (should be false)
    ('1506715214', True),   # Valid ISBN-10 without hyphens
    ('9780470059028', True), # Valid ISBN-10 example from the function documentation
    ('978-0-470-05902-8', False), # Invalid ISBN-10 with hyphens (should be false)
])
def test_valid_isbn_10(input_string, expected):
    assert is_isbn_10(input_string) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_10_0_test_valid_isbn_10.py F [ 25%]
.F.                                                                      [100%]

=================================== FAILURES ===================================
____________________ test_valid_isbn_10[150-6715214-False] _____________________

input_string = '150-6715214', expected = False

    @pytest.mark.parametrize("input_string, expected", [
        ('150-6715214', False),  # Invalid ISBN-10 with hyphens (should be false)
        ('1506715214', True),   # Valid ISBN-10 without hyphens
        ('9780470059028', True), # Valid ISBN-10 example from the function documentation
        ('978-0-470-05902-8', False), # Invalid ISBN-10 with hyphens (should be false)
    ])
    def test_valid_isbn_10(input_string, expected):
>       assert is_isbn_10(input_string) == expected
E       AssertionError: assert True == False
E        +  where True = is_isbn_10('150-6715214')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_10_0_test_valid_isbn_10.py:12: AssertionError
____________________ test_valid_isbn_10[9780470059028-True] ____________________

input_string = '9780470059028', expected = True

    @pytest.mark.parametrize("input_string, expected", [
        ('150-6715214', False),  # Invalid ISBN-10 with hyphens (should be false)
        ('1506715214', True),   # Valid ISBN-10 without hyphens
        ('9780470059028', True), # Valid ISBN-10 example from the function documentation
        ('978-0-470-05902-8', False), # Invalid ISBN-10 with hyphens (should be false)
    ])
    def test_valid_isbn_10(input_string, expected):
>       assert is_isbn_10(input_string) == expected
E       AssertionError: assert False == True
E        +  where False = is_isbn_10('9780470059028')

python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_10_0_test_valid_isbn_10.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_10_0_test_valid_isbn_10.py::test_valid_isbn_10[150-6715214-False]
FAILED python-string-utils/Test4DT_tests/test_string_utils_validation_is_isbn_10_0_test_valid_isbn_10.py::test_valid_isbn_10[9780470059028-True]
========================= 2 failed, 2 passed in 0.03s ==========================
"""