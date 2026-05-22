
import unittest.mock as mock
from httpie.output.ui.rich_utils import enable_highlighter
from rich.console import Console
from rich.highlighter import Highlighter

def test_enable_highlighter():
    # Create a mock Console instance
    console = mock.create_autospec(Console)
    
    # Create a mock Highlighter instance
    highlighter = mock.create_autospec(Highlighter)
    
    # Mock the original highlighter to be None initially
    console.highlighter = None
    
    with mock.patch('httpie.output.ui.rich_utils.enable_highlighter') as mock_enable:
        # Call the function under test
        enable_highlighter(console, highlighter)
        
        # Assert that the original highlighter was set correctly
        assert console.highlighter == highlighter

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_utils_enable_highlighter_0_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
___________________________ test_enable_highlighter ____________________________

    def test_enable_highlighter():
        # Create a mock Console instance
        console = mock.create_autospec(Console)
    
        # Create a mock Highlighter instance
        highlighter = mock.create_autospec(Highlighter)
    
        # Mock the original highlighter to be None initially
        console.highlighter = None
    
        with mock.patch('httpie.output.ui.rich_utils.enable_highlighter') as mock_enable:
            # Call the function under test
            enable_highlighter(console, highlighter)
    
            # Assert that the original highlighter was set correctly
>           assert console.highlighter == highlighter
E           AssertionError: assert None == <MagicMock spec='Highlighter' id='140234775437904'>
E            +  where None = <MagicMock spec='Console' id='140234774964752'>.highlighter

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_utils_enable_highlighter_0_test_edge_cases.py:22: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_ui_rich_utils_enable_highlighter_0_test_edge_cases.py::test_enable_highlighter
============================== 1 failed in 0.24s ===============================
"""