
import pytest
from isort.format import BasicPrinter
from io import StringIO

@pytest.fixture
def printer():
    return BasicPrinter(error='An error occurred', success='Operation successful')

def test_invalid_input(printer):
    output = StringIO()
    printer.output = output
    
    # Test with invalid input
    with pytest.raises(TypeError):
        printer.print_success(123)  # Invalid input type
    
    assert "An error occurred: An error occurred - 123" not in output.getvalue()

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

isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

printer = <isort.format.BasicPrinter object at 0x7fa66f2aa010>

    def test_invalid_input(printer):
        output = StringIO()
        printer.output = output
    
        # Test with invalid input
        with pytest.raises(TypeError):
>           printer.print_success(123)  # Invalid input type
E           AttributeError: 'BasicPrinter' object has no attribute 'print_success'

isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_invalid_input.py:16: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_BasicPrinter_success_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.16s ===============================
"""