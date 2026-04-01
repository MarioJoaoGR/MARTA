
import pytest
from string_utils.manipulation import __RomanNumbers

def test_valid_case_1():
    assert __RomanNumbers.__encode_digit(0, 3) == 'III'

def test_valid_case_2():
    assert __RomanNumbers.__encode_digit(1, 4) == 'IV'

def test_valid_case_3():
    assert __RomanNumbers.__encode_digit(2, 9) == 'IX'

def test_valid_case_4():
    assert __RomanNumbers.__encode_digit(3, 58) == 'LVIII'

def test_valid_case_5():
    assert __RomanNumbers.__encode_digit(0, 0) == ''

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_valid_case_1.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
______________________________ test_valid_case_1 _______________________________

    def test_valid_case_1():
>       assert __RomanNumbers.__encode_digit(0, 3) == 'III'
E       AttributeError: type object '__RomanNumbers' has no attribute '__encode_digit'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_valid_case_1.py:6: AttributeError
______________________________ test_valid_case_2 _______________________________

    def test_valid_case_2():
>       assert __RomanNumbers.__encode_digit(1, 4) == 'IV'
E       AttributeError: type object '__RomanNumbers' has no attribute '__encode_digit'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_valid_case_1.py:9: AttributeError
______________________________ test_valid_case_3 _______________________________

    def test_valid_case_3():
>       assert __RomanNumbers.__encode_digit(2, 9) == 'IX'
E       AttributeError: type object '__RomanNumbers' has no attribute '__encode_digit'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_valid_case_1.py:12: AttributeError
______________________________ test_valid_case_4 _______________________________

    def test_valid_case_4():
>       assert __RomanNumbers.__encode_digit(3, 58) == 'LVIII'
E       AttributeError: type object '__RomanNumbers' has no attribute '__encode_digit'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_valid_case_1.py:15: AttributeError
______________________________ test_valid_case_5 _______________________________

    def test_valid_case_5():
>       assert __RomanNumbers.__encode_digit(0, 0) == ''
E       AttributeError: type object '__RomanNumbers' has no attribute '__encode_digit'

python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_valid_case_1.py:18: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_valid_case_1.py::test_valid_case_1
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_valid_case_1.py::test_valid_case_2
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_valid_case_1.py::test_valid_case_3
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_valid_case_1.py::test_valid_case_4
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___RomanNumbers___encode_digit_0_test_valid_case_1.py::test_valid_case_5
============================== 5 failed in 0.03s ===============================
"""