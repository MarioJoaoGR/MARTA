
import pytest
from unittest.mock import patch, Mock
from httpie.output.formatters.colors import get_available_styles

def test_get_available_styles():
    # Create a mock for the Pygments styles module
    mock_pygments_styles = Mock()
    mock_pygments_styles.get_all_styles.return_value = ['monokai', 'default']
    
    with patch('httpie.output.formatters.colors.pygments.styles', mock_pygments_styles):
        # Call the function under test
        available_styles = get_available_styles()
        
        # Assert that the function returns a sorted list of styles
        assert isinstance(available_styles, list), "Expected a list"
        assert set(available_styles) == {'monokai', 'default'}, "Unexpected style names"
        assert available_styles == ['default', 'monokai'], "List is not sorted alphabetically"

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_available_styles_1_test_error_case.py F [100%]

=================================== FAILURES ===================================
__________________________ test_get_available_styles ___________________________

    def test_get_available_styles():
        # Create a mock for the Pygments styles module
        mock_pygments_styles = Mock()
        mock_pygments_styles.get_all_styles.return_value = ['monokai', 'default']
    
        with patch('httpie.output.formatters.colors.pygments.styles', mock_pygments_styles):
            # Call the function under test
            available_styles = get_available_styles()
    
            # Assert that the function returns a sorted list of styles
            assert isinstance(available_styles, list), "Expected a list"
>           assert set(available_styles) == {'monokai', 'default'}, "Unexpected style names"
E           AssertionError: Unexpected style names
E           assert {'auto', 'def...-light'>, ...} == {'default', 'monokai'}
E             
E             Extra items in the left set:
E             'auto'
E             <PieStyle.DARK: 'pie-dark'>
E             <PieStyle.UNIVERSAL: 'pie'>
E             <PieStyle.LIGHT: 'pie-light'>
E             'solarized'
E             Use -v to get more diff

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_available_styles_1_test_error_case.py:17: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_output_formatters_colors_get_available_styles_1_test_error_case.py::test_get_available_styles
============================== 1 failed in 0.32s ===============================
"""