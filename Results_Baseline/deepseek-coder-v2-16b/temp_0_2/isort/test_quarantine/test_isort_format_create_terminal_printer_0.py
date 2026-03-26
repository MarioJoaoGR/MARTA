
# Module: isort.format
import pytest
from io import StringIO
from isort.format import create_terminal_printer
from isort.format import BasicPrinter
from isort.format import ColoramaPrinter
import sys
try:
    import colorama
except ImportError:
    pass

# Fixture to mock the behavior of colorama being unavailable
@pytest.fixture(autouse=True)
def mock_colorama_unavailable():
    original_value = getattr(sys, 'colorama_unavailable', False)
    setattr(sys, 'colorama_unavailable', True)
    yield
    setattr(sys, 'colorama_unavailable', original_value)

def test_create_terminal_printer_with_color():
    output = StringIO()
    sys.stdout = output
    printer = create_terminal_printer(color=True, output=output, error="ERROR", success="SUCCESS")
    assert isinstance(printer, ColoramaPrinter)
    assert printer._error == "ERROR"
    assert printer._success == "SUCCESS"
    assert printer._output == output
    sys.stdout = sys.__stdout__

def test_create_terminal_printer_without_color():
    output = StringIO()
    sys.stdout = output
    printer = create_terminal_printer(color=False, output=output, error="ERROR", success="SUCCESS")
    assert isinstance(printer, BasicPrinter)
    assert printer._error == "ERROR"
    assert printer._success == "SUCCESS"
    assert printer._output == output
    sys.stdout = sys.__stdout__

def test_create_terminal_printer_without_colorama():
    with pytest.raises(SystemExit):
        create_terminal_printer(color=True, output=sys.stdout)

def test_create_terminal_printer_with_default_output():
    sys.stdout = StringIO()
    printer = create_terminal_printer(color=False, error="ERROR", success="SUCCESS")
    assert isinstance(printer, BasicPrinter)
    assert printer._error == "ERROR"
    assert printer._success == "SUCCESS"
    assert printer._output == sys.stdout
    sys.stdout = sys.__stdout__

def test_create_terminal_printer_with_custom_output():
    output = StringIO()
    sys.stdout = output
    printer = create_terminal_printer(color=False, output=output, error="ERROR", success="SUCCESS")
    assert isinstance(printer, BasicPrinter)
    assert printer._error == "ERROR"
    assert printer._success == "SUCCESS"
    assert printer._output == output
    sys.stdout = sys.__stdout__

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_format_create_terminal_printer_0
isort/Test4DT_tests/test_isort_format_create_terminal_printer_0.py:27:11: E1101: Instance of 'ColoramaPrinter' has no '_error' member; maybe 'error'? (no-member)
isort/Test4DT_tests/test_isort_format_create_terminal_printer_0.py:28:11: E1101: Instance of 'ColoramaPrinter' has no '_success' member; maybe 'success'? (no-member)
isort/Test4DT_tests/test_isort_format_create_terminal_printer_0.py:29:11: E1101: Instance of 'ColoramaPrinter' has no '_output' member; maybe 'output'? (no-member)
isort/Test4DT_tests/test_isort_format_create_terminal_printer_0.py:37:11: E1101: Instance of 'BasicPrinter' has no '_error' member; maybe 'error'? (no-member)
isort/Test4DT_tests/test_isort_format_create_terminal_printer_0.py:38:11: E1101: Instance of 'BasicPrinter' has no '_success' member; maybe 'success'? (no-member)
isort/Test4DT_tests/test_isort_format_create_terminal_printer_0.py:39:11: E1101: Instance of 'BasicPrinter' has no '_output' member; maybe 'output'? (no-member)
isort/Test4DT_tests/test_isort_format_create_terminal_printer_0.py:50:11: E1101: Instance of 'BasicPrinter' has no '_error' member; maybe 'error'? (no-member)
isort/Test4DT_tests/test_isort_format_create_terminal_printer_0.py:51:11: E1101: Instance of 'BasicPrinter' has no '_success' member; maybe 'success'? (no-member)
isort/Test4DT_tests/test_isort_format_create_terminal_printer_0.py:52:11: E1101: Instance of 'BasicPrinter' has no '_output' member; maybe 'output'? (no-member)
isort/Test4DT_tests/test_isort_format_create_terminal_printer_0.py:60:11: E1101: Instance of 'BasicPrinter' has no '_error' member; maybe 'error'? (no-member)
isort/Test4DT_tests/test_isort_format_create_terminal_printer_0.py:61:11: E1101: Instance of 'BasicPrinter' has no '_success' member; maybe 'success'? (no-member)
isort/Test4DT_tests/test_isort_format_create_terminal_printer_0.py:62:11: E1101: Instance of 'BasicPrinter' has no '_output' member; maybe 'output'? (no-member)


"""