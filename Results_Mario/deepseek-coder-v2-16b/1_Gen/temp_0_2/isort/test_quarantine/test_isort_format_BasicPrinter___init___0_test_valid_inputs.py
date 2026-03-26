
import pytest
from io import StringIO
from isort.format import BasicPrinter

@pytest.fixture
def setup_printer():
    error_message = "Error occurred"
    success_message = "Operation succeeded"
    output = StringIO()
    printer = BasicPrinter(error=error_message, success=success_message, output=output)
    return (printer, output)

def test_valid_inputs(setup_printer):
    printer, mock_output = setup_printer
    
    # Test print_success method
    message = 'The operation was successful!'
    printer.print_success(message)
    
    # Assert that the success message is written to the output
    mock_output.seek(0)  # Move to the beginning of the stream
    assert "SUCCESS: The operation was successful!" in mock_output.read()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_format_BasicPrinter___init___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

setup_printer = (<isort.format.BasicPrinter object at 0x7f732d8ac790>, <_io.StringIO object at 0x7f732d3bce50>)

    def test_valid_inputs(setup_printer):
        printer, mock_output = setup_printer
    
        # Test print_success method
        message = 'The operation was successful!'
>       printer.print_success(message)
E       AttributeError: 'BasicPrinter' object has no attribute 'print_success'

isort/Test4DT_tests/test_isort_format_BasicPrinter___init___0_test_valid_inputs.py:19: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_BasicPrinter___init___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.10s ===============================
"""