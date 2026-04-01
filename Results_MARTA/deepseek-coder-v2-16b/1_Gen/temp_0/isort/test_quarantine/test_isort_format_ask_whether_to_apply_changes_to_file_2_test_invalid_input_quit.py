
import sys
from unittest.mock import patch
import pytest

def ask_whether_to_apply_changes_to_file(file_path: str) -> bool:
    answer = None
    while answer not in ("yes", "y", "no", "n", "quit", "q"):
        answer = input(f"Apply suggested changes to '{file_path}' [y/n/q]? ")  # nosec
        answer = answer.lower()
        if answer in ("no", "n"):
            return False
        if answer in ("quit", "q"):
            sys.exit(1)
    return True

@pytest.mark.parametrize("mock_input, expected", [('y', True), ('n', False), ('q', pytest.raises(SystemExit))])
def test_invalid_input_quit(mock_input, expected):
    with patch('builtins.input', return_value=mock_input):
        if isinstance(expected, type) and issubclass(expected, BaseException):
            with pytest.raises(expected):
                ask_whether_to_apply_changes_to_file("example.txt")
        else:
            assert ask_whether_to_apply_changes_to_file("example.txt") == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

isort/Test4DT_tests/test_isort_format_ask_whether_to_apply_changes_to_file_2_test_invalid_input_quit.py . [ 33%]
.F                                                                       [100%]

=================================== FAILURES ===================================
_____________________ test_invalid_input_quit[q-expected2] _____________________

mock_input = 'q'
expected = <_pytest.python_api.RaisesContext object at 0x7fc54818cd90>

    @pytest.mark.parametrize("mock_input, expected", [('y', True), ('n', False), ('q', pytest.raises(SystemExit))])
    def test_invalid_input_quit(mock_input, expected):
        with patch('builtins.input', return_value=mock_input):
            if isinstance(expected, type) and issubclass(expected, BaseException):
                with pytest.raises(expected):
                    ask_whether_to_apply_changes_to_file("example.txt")
            else:
>               assert ask_whether_to_apply_changes_to_file("example.txt") == expected

isort/Test4DT_tests/test_isort_format_ask_whether_to_apply_changes_to_file_2_test_invalid_input_quit.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

file_path = 'example.txt'

    def ask_whether_to_apply_changes_to_file(file_path: str) -> bool:
        answer = None
        while answer not in ("yes", "y", "no", "n", "quit", "q"):
            answer = input(f"Apply suggested changes to '{file_path}' [y/n/q]? ")  # nosec
            answer = answer.lower()
            if answer in ("no", "n"):
                return False
            if answer in ("quit", "q"):
>               sys.exit(1)
E               SystemExit: 1

isort/Test4DT_tests/test_isort_format_ask_whether_to_apply_changes_to_file_2_test_invalid_input_quit.py:14: SystemExit
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_ask_whether_to_apply_changes_to_file_2_test_invalid_input_quit.py::test_invalid_input_quit[q-expected2]
========================= 1 failed, 2 passed in 0.07s ==========================
"""