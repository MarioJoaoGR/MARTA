
from string_utils.manipulation import __RomanNumbers

def test_valid_case_1():
    # Test cases for each digit position (units, tens, hundreds, thousands)
    test_cases = [
        (0, 1, 'I'),
        (0, 2, 'II'),
        (0, 3, 'III'),
        (0, 4, 'IV'),
        (0, 5, 'V'),
        (0, 6, 'VI'),
        (0, 7, 'VII'),
        (0, 8, 'VIII'),
        (0, 9, 'IX'),
        (1, 1, 'X'),
        (1, 2, 'XX'),
        (1, 3, 'XXX'),
        (1, 4, 'XL'),
        (1, 5, 'L'),
        (1, 6, 'LX'),
        (1, 7, 'LXX'),
        (1, 8, 'LXXX'),
        (1, 9, 'XC'),
        (2, 1, 'C'),
        (2, 2, 'CC'),
        (2, 3, 'CCC'),
        (2, 4, 'CD'),
        (2, 5, 'D'),
        (2, 6, 'DC'),
        (2, 7, 'DCC'),
        (2, 8, 'DCCC'),
        (2, 9, 'CM'),
        (3, 1, 'M'),
        (3, 2, 'MM'),
        (3, 3, 'MMM')
    ]
    
    for index, value, expected in test_cases:
        assert __RomanNumbers.__encode_digit(index, value) == expected, f"Failed for index={index}, value={value}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_valid_case_1.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_case_1 _______________________________

    def test_valid_case_1():
        # Test cases for each digit position (units, tens, hundreds, thousands)
        test_cases = [
            (0, 1, 'I'),
            (0, 2, 'II'),
            (0, 3, 'III'),
            (0, 4, 'IV'),
            (0, 5, 'V'),
            (0, 6, 'VI'),
            (0, 7, 'VII'),
            (0, 8, 'VIII'),
            (0, 9, 'IX'),
            (1, 1, 'X'),
            (1, 2, 'XX'),
            (1, 3, 'XXX'),
            (1, 4, 'XL'),
            (1, 5, 'L'),
            (1, 6, 'LX'),
            (1, 7, 'LXX'),
            (1, 8, 'LXXX'),
            (1, 9, 'XC'),
            (2, 1, 'C'),
            (2, 2, 'CC'),
            (2, 3, 'CCC'),
            (2, 4, 'CD'),
            (2, 5, 'D'),
            (2, 6, 'DC'),
            (2, 7, 'DCC'),
            (2, 8, 'DCCC'),
            (2, 9, 'CM'),
            (3, 1, 'M'),
            (3, 2, 'MM'),
            (3, 3, 'MMM')
        ]
    
        for index, value, expected in test_cases:
>           assert __RomanNumbers.__encode_digit(index, value) == expected, f"Failed for index={index}, value={value}"
E           AttributeError: type object '__RomanNumbers' has no attribute '__encode_digit'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_valid_case_1.py:40: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_valid_case_1.py::test_valid_case_1
============================== 1 failed in 0.02s ===============================
"""