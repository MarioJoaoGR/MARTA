
from string_utils.manipulation import __StringFormatter, InvalidInputError
import re

def test_valid_input():
    # Arrange
    input_string = "Hello World"
    
    # Act
    formatter = __StringFormatter(input_string)
    
    # Assert
    assert formatter.input_string == "Hello World "

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_right_space_only_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        # Arrange
        input_string = "Hello World"
    
        # Act
        formatter = __StringFormatter(input_string)
    
        # Assert
>       assert formatter.input_string == "Hello World "
E       AssertionError: assert 'Hello World' == 'Hello World '
E         
E         - Hello World 
E         ?            -
E         + Hello World

python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_right_space_only_0_test_valid_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation___StringFormatter___ensure_right_space_only_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.03s ===============================
"""