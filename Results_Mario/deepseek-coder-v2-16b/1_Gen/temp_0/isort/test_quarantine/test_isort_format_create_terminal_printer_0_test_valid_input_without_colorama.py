
import pytest
from io import StringIO
from isort.format import create_terminal_printer, ColoramaPrinter, BasicPrinter
import sys
from unittest.mock import patch

# Mocking colorama not being available
class MockColoramaUnavailable:
    def __getattr__(self, name):
        raise ModuleNotFoundError(f"No module named 'colorama'")

@pytest.fixture(autouse=True)
def mock_colorama_unavailable():
    sys.modules['colorama'] = MockColoramaUnavailable()

# Test cases
@pytest.mark.parametrize("color, expected", [(True, ColoramaPrinter), (False, BasicPrinter)])
def test_valid_input_without_colorama(color, expected):
    output = StringIO()
    result = create_terminal_printer(color, output, "Error message", "Success message")
    
    assert isinstance(result, expected)
    if color:
        # Since we are mocking, check that the initialization of ColoramaPrinter happened correctly.
        with patch('colorama.init') as mock_init:
            mock_init.assert_called_once()
    else:
        # Check that no action is taken for init in case colorama is unavailable.
        with patch('colorama.init') as mock_init:
            assert not mock_init.called

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

isort/Test4DT_tests/test_isort_format_create_terminal_printer_0_test_valid_input_without_colorama.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________ test_valid_input_without_colorama[True-ColoramaPrinter] ____________

color = True, expected = <class 'isort.format.ColoramaPrinter'>

    @pytest.mark.parametrize("color, expected", [(True, ColoramaPrinter), (False, BasicPrinter)])
    def test_valid_input_without_colorama(color, expected):
        output = StringIO()
>       result = create_terminal_printer(color, output, "Error message", "Success message")

isort/Test4DT_tests/test_isort_format_create_terminal_printer_0_test_valid_input_without_colorama.py:21: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

color = True, output = <_io.StringIO object at 0x7fbe9aa91a20>
error = 'Error message', success = 'Success message'

    def create_terminal_printer(
        color: bool, output: TextIO | None = None, error: str = "", success: str = ""
    ) -> BasicPrinter:
        if color and colorama_unavailable:
            no_colorama_message = (
                "\n"
                "Sorry, but to use --color (color_output) the colorama python package is required.\n\n"
                "Reference: https://pypi.org/project/colorama/\n\n"
                "You can either install it separately on your system or as the colors extra "
                "for isort. Ex: \n\n"
                "$ pip install isort[colors]\n"
            )
            print(no_colorama_message, file=sys.stderr)
>           sys.exit(1)
E           SystemExit: 1

isort/isort/format.py:151: SystemExit
----------------------------- Captured stderr call -----------------------------

Sorry, but to use --color (color_output) the colorama python package is required.

Reference: https://pypi.org/project/colorama/

You can either install it separately on your system or as the colors extra for isort. Ex: 

$ pip install isort[colors]

____________ test_valid_input_without_colorama[False-BasicPrinter] _____________

color = False, expected = <class 'isort.format.BasicPrinter'>

    @pytest.mark.parametrize("color, expected", [(True, ColoramaPrinter), (False, BasicPrinter)])
    def test_valid_input_without_colorama(color, expected):
        output = StringIO()
        result = create_terminal_printer(color, output, "Error message", "Success message")
    
        assert isinstance(result, expected)
        if color:
            # Since we are mocking, check that the initialization of ColoramaPrinter happened correctly.
            with patch('colorama.init') as mock_init:
                mock_init.assert_called_once()
        else:
            # Check that no action is taken for init in case colorama is unavailable.
>           with patch('colorama.init') as mock_init:

isort/Test4DT_tests/test_isort_format_create_terminal_printer_0_test_valid_input_without_colorama.py:30: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/unittest/mock.py:1430: in __enter__
    self.target = self.getter()
/usr/local/lib/python3.11/pkgutil.py:700: in resolve_name
    mod = importlib.import_module(modname)
/usr/local/lib/python3.11/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
<frozen importlib._bootstrap>:1204: in _gcd_import
    ???
<frozen importlib._bootstrap>:1172: in _find_and_load
    ???
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Test4DT_tests.test_isort_format_create_terminal_printer_0_test_valid_input_without_colorama.MockColoramaUnavailable object at 0x7fbe9abfa310>
name = '__spec__'

    def __getattr__(self, name):
>       raise ModuleNotFoundError(f"No module named 'colorama'")
E       ModuleNotFoundError: No module named 'colorama'

isort/Test4DT_tests/test_isort_format_create_terminal_printer_0_test_valid_input_without_colorama.py:11: ModuleNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_format_create_terminal_printer_0_test_valid_input_without_colorama.py::test_valid_input_without_colorama[True-ColoramaPrinter]
FAILED isort/Test4DT_tests/test_isort_format_create_terminal_printer_0_test_valid_input_without_colorama.py::test_valid_input_without_colorama[False-BasicPrinter]
============================== 2 failed in 0.17s ===============================
"""