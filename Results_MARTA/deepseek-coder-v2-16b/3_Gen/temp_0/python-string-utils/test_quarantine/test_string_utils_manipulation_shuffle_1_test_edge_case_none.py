
import pytest
from unittest.mock import patch
from string_utils.manipulation import shuffle
from string_utils.errors import InvalidInputError

def test_edge_case_none():
    with pytest.raises(InvalidInputError) as exc_info:
        shuffle(None)
    assert str(exc_info.value) == "Expected 'str', received '<class 'NoneType'>'"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/python-string-utils
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

python-string-utils/Test4DT_tests/test_string_utils_manipulation_shuffle_1_test_edge_case_none.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_edge_case_none ______________________________

    def test_edge_case_none():
        with pytest.raises(InvalidInputError) as exc_info:
            shuffle(None)
>       assert str(exc_info.value) == "Expected 'str', received '<class 'NoneType'>'"
E       assert 'Expected "st...ed "NoneType"' == "Expected 'st... 'NoneType'>'"
E         
E         - Expected 'str', received '<class 'NoneType'>'
E         ?          ^   ^           ^^^^^^^^^        ^^^
E         + Expected "str", received "NoneType"
E         ?          ^   ^           ^        ^

python-string-utils/Test4DT_tests/test_string_utils_manipulation_shuffle_1_test_edge_case_none.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED python-string-utils/Test4DT_tests/test_string_utils_manipulation_shuffle_1_test_edge_case_none.py::test_edge_case_none
============================== 1 failed in 0.03s ===============================
"""