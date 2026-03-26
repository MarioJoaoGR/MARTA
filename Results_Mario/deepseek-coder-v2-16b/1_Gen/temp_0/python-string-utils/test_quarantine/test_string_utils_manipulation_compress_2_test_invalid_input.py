
import pytest
from string_utils.manipulation import compress

def test_invalid_input():
    with pytest.raises(ValueError) as e:
        compress('')
    assert str(e.value) == 'Input string must not be empty'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_compress_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(ValueError) as e:
            compress('')
>       assert str(e.value) == 'Input string must not be empty'
E       AssertionError: assert 'Input string cannot be empty' == 'Input string... not be empty'
E         
E         - Input string must not be empty
E         ?              ^^^^^
E         + Input string cannot be empty
E         ?              ^^^

python-string-utils/Test4DT_tests/test_string_utils_manipulation_compress_2_test_invalid_input.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_compress_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.03s ===============================

"""