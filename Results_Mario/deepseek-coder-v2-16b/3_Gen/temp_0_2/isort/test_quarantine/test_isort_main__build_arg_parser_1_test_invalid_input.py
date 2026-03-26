
import argparse
from unittest.mock import patch
import pytest
from isort.main import _build_arg_parser

@pytest.mark.parametrize("input_args", [
    (["--invalid-option"]),  # Invalid option
    ([""]),                  # No arguments
    (["--help"]),            # Help flag
])
def test_invalid_input(input_args):
    with patch('sys.argv', ['isort'] + input_args):
        with pytest.raises(SystemExit) as excinfo:
            _build_arg_parser()
    assert excinfo.type == SystemExit

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

isort/Test4DT_tests/test_isort_main__build_arg_parser_1_test_invalid_input.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________ test_invalid_input[input_args0] ________________________

input_args = ['--invalid-option']

    @pytest.mark.parametrize("input_args", [
        (["--invalid-option"]),  # Invalid option
        ([""]),                  # No arguments
        (["--help"]),            # Help flag
    ])
    def test_invalid_input(input_args):
        with patch('sys.argv', ['isort'] + input_args):
>           with pytest.raises(SystemExit) as excinfo:
E           Failed: DID NOT RAISE <class 'SystemExit'>

isort/Test4DT_tests/test_isort_main__build_arg_parser_1_test_invalid_input.py:14: Failed
_______________________ test_invalid_input[input_args1] ________________________

input_args = ['']

    @pytest.mark.parametrize("input_args", [
        (["--invalid-option"]),  # Invalid option
        ([""]),                  # No arguments
        (["--help"]),            # Help flag
    ])
    def test_invalid_input(input_args):
        with patch('sys.argv', ['isort'] + input_args):
>           with pytest.raises(SystemExit) as excinfo:
E           Failed: DID NOT RAISE <class 'SystemExit'>

isort/Test4DT_tests/test_isort_main__build_arg_parser_1_test_invalid_input.py:14: Failed
_______________________ test_invalid_input[input_args2] ________________________

input_args = ['--help']

    @pytest.mark.parametrize("input_args", [
        (["--invalid-option"]),  # Invalid option
        ([""]),                  # No arguments
        (["--help"]),            # Help flag
    ])
    def test_invalid_input(input_args):
        with patch('sys.argv', ['isort'] + input_args):
>           with pytest.raises(SystemExit) as excinfo:
E           Failed: DID NOT RAISE <class 'SystemExit'>

isort/Test4DT_tests/test_isort_main__build_arg_parser_1_test_invalid_input.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_main__build_arg_parser_1_test_invalid_input.py::test_invalid_input[input_args0]
FAILED isort/Test4DT_tests/test_isort_main__build_arg_parser_1_test_invalid_input.py::test_invalid_input[input_args1]
FAILED isort/Test4DT_tests/test_isort_main__build_arg_parser_1_test_invalid_input.py::test_invalid_input[input_args2]
============================== 3 failed in 0.13s ===============================
"""