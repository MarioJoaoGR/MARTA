
import pytest
from unittest.mock import MagicMock
from isort.main import _print_hard_fail

def test_print_hard_fail(monkeypatch):
    # Mock the config object with color_output set to True and format_error set to "Error: {message}"
    mock_config = MagicMock()
    mock_config.color_output = True
    mock_config.format_error = "Error: {message}"
    
    # Monkeypatch sys.exit to prevent actual exit
    monkeypatch.setattr('sys.exit', lambda x: None)
    
    # Call the function with the mocked config and a custom message
    _print_hard_fail(config=mock_config, message="A critical error occurred.")

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

isort/Test4DT_tests/test_isort_main__print_hard_fail_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_print_hard_fail _____________________________

monkeypatch = <_pytest.monkeypatch.MonkeyPatch object at 0x7f5e9332f950>

    def test_print_hard_fail(monkeypatch):
        # Mock the config object with color_output set to True and format_error set to "Error: {message}"
        mock_config = MagicMock()
        mock_config.color_output = True
        mock_config.format_error = "Error: {message}"
    
        # Monkeypatch sys.exit to prevent actual exit
        monkeypatch.setattr('sys.exit', lambda x: None)
    
        # Call the function with the mocked config and a custom message
>       _print_hard_fail(config=mock_config, message="A critical error occurred.")

isort/Test4DT_tests/test_isort_main__print_hard_fail_0_test_edge_cases.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
isort/isort/main.py:129: in _print_hard_fail
    printer = create_terminal_printer(
isort/isort/format.py:156: in create_terminal_printer
    ColoramaPrinter(error, success, output) if color else BasicPrinter(error, success, output)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <isort.format.ColoramaPrinter object at 0x7f5e92ff8410>
error = 'Error: {message}'
success = <MagicMock name='mock.format_success' id='140044169872464'>
output = None

    def __init__(self, error: str, success: str, output: TextIO | None):
        super().__init__(error, success, output=output)
    
        # Note: this constants are instance variables instead ofs class variables
        # because they refer to colorama which might not be installed.
>       self.ERROR = self.style_text("ERROR", colorama.Fore.RED)
E       NameError: name 'colorama' is not defined

isort/isort/format.py:118: NameError
----------------------------- Captured stderr call -----------------------------

Sorry, but to use --color (color_output) the colorama python package is required.

Reference: https://pypi.org/project/colorama/

You can either install it separately on your system or as the colors extra for isort. Ex: 

$ pip install isort[colors]

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_main__print_hard_fail_0_test_edge_cases.py::test_print_hard_fail
============================== 1 failed in 0.14s ===============================
"""