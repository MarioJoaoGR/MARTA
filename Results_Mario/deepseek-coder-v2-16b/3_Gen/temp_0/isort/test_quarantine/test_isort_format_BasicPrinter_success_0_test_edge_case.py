
from isort.format import BasicPrinter
import sys
from unittest.mock import MagicMock, patch

def test_print_success():
    printer = BasicPrinter(error='ERROR', success='SUCCESS')
    with patch('sys.stdout', new=MagicMock()) as mock_stdout:
        printer.success('Hello, world!')
        assert mock_stdout.write.called
        expected_output = 'SUCCESS: Hello, world!\n'
        assert mock_stdout.write.call_args[0][0] == expected_output

def test_print_error():
    printer = BasicPrinter(error='ERROR', success='SUCCESS')
    with patch('sys.stderr', new=MagicMock()) as mock_stderr:
        printer.error('Something went wrong.')
        assert mock_stderr.write.called
        expected_output = 'ERROR: Something went wrong.\n'
        assert mock_stderr.write.call_args[0][0] == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_edge_case.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_print_success ______________________________

    def test_print_success():
        printer = BasicPrinter(error='ERROR', success='SUCCESS')
        with patch('sys.stdout', new=MagicMock()) as mock_stdout:
            printer.success('Hello, world!')
>           assert mock_stdout.write.called
E           AssertionError: assert False
E            +  where False = <MagicMock name='mock.write' id='140511129390608'>.called
E            +    where <MagicMock name='mock.write' id='140511129390608'> = <MagicMock id='140511129547856'>.write

isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_edge_case.py:10: AssertionError
----------------------------- Captured stdout call -----------------------------
SUCCESS
_______________________________ test_print_error _______________________________

    def test_print_error():
        printer = BasicPrinter(error='ERROR', success='SUCCESS')
        with patch('sys.stderr', new=MagicMock()) as mock_stderr:
            printer.error('Something went wrong.')
            assert mock_stderr.write.called
            expected_output = 'ERROR: Something went wrong.\n'
>           assert mock_stderr.write.call_args[0][0] == expected_output
E           AssertionError: assert '\n' == 'ERROR: Somet...went wrong.\n'
E             
E             Strings contain only whitespace, escaping them using repr()
E             - 'ERROR: Something went wrong.\n'
E             + '\n'

isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_edge_case.py:20: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_edge_case.py::test_print_success
FAILED isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_edge_case.py::test_print_error
============================== 2 failed in 0.13s ===============================
"""