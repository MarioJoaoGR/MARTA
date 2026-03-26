
import pytest
from superstring.superstring import SuperStringBase, SuperStringUpper  # Assuming this module contains the classes

# Define test data
test_data = [
    (None, None, 'HELLO WORLD!'),
    (6, None, 'WORLD!'),
    (None, 5, 'HEL'),
    (3, 7, 'LO W')
]

@pytest.mark.parametrize("start_index, end_index, expected", test_data)
def test_to_printable(start_index, end_index, expected):
    left_string = SuperStringBase("Hello")
    right_string = SuperStringBase("World!")
    concatenated = SuperStringUpper(left_string + right_string)  # Concatenate and instantiate SuperStringUpper
    assert concatenated.to_printable(start_index, end_index).upper() == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 4 items

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_valid_input_with_start_index.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
__________________ test_to_printable[None-None-HELLO WORLD!] ___________________

start_index = None, end_index = None, expected = 'HELLO WORLD!'

    @pytest.mark.parametrize("start_index, end_index, expected", test_data)
    def test_to_printable(start_index, end_index, expected):
>       left_string = SuperStringBase("Hello")
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_valid_input_with_start_index.py:15: TypeError
_______________________ test_to_printable[6-None-WORLD!] _______________________

start_index = 6, end_index = None, expected = 'WORLD!'

    @pytest.mark.parametrize("start_index, end_index, expected", test_data)
    def test_to_printable(start_index, end_index, expected):
>       left_string = SuperStringBase("Hello")
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_valid_input_with_start_index.py:15: TypeError
________________________ test_to_printable[None-5-HEL] _________________________

start_index = None, end_index = 5, expected = 'HEL'

    @pytest.mark.parametrize("start_index, end_index, expected", test_data)
    def test_to_printable(start_index, end_index, expected):
>       left_string = SuperStringBase("Hello")
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_valid_input_with_start_index.py:15: TypeError
_________________________ test_to_printable[3-7-LO W] __________________________

start_index = 3, end_index = 7, expected = 'LO W'

    @pytest.mark.parametrize("start_index, end_index, expected", test_data)
    def test_to_printable(start_index, end_index, expected):
>       left_string = SuperStringBase("Hello")
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_valid_input_with_start_index.py:15: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_valid_input_with_start_index.py::test_to_printable[None-None-HELLO WORLD!]
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_valid_input_with_start_index.py::test_to_printable[6-None-WORLD!]
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_valid_input_with_start_index.py::test_to_printable[None-5-HEL]
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_to_printable_0_test_valid_input_with_start_index.py::test_to_printable[3-7-LO W]
============================== 4 failed in 0.05s ===============================
"""