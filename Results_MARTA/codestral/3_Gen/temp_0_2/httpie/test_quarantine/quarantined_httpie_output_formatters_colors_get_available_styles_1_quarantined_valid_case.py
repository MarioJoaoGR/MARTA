
import pytest
from unittest.mock import patch
from httpie.output.formatters.colors import get_available_styles

def test_get_available_styles():
    with patch('httpie.output.formatters.colors.pygments.styles.get_all_styles') as mock_get_all_styles:
        # Mock the return value of get_all_styles to simulate available styles
        mock_get_all_styles.return_value = ['monokai', 'default', 'friendly']
        
        # Call the function under test
        available_styles = get_available_styles()
        
        # Assert that the returned list is sorted and includes mocked styles
        assert available_styles == ['default', 'friendly', 'monokai']

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

httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_get_available_styles_1_test_valid_case.py F [100%]

=================================== FAILURES ===================================
__________________________ test_get_available_styles ___________________________

    def test_get_available_styles():
        with patch('httpie.output.formatters.colors.pygments.styles.get_all_styles') as mock_get_all_styles:
            # Mock the return value of get_all_styles to simulate available styles
            mock_get_all_styles.return_value = ['monokai', 'default', 'friendly']
    
            # Call the function under test
            available_styles = get_available_styles()
    
            # Assert that the returned list is sorted and includes mocked styles
>           assert available_styles == ['default', 'friendly', 'monokai']
E           AssertionError: assert ['auto', 'def...e-dark'>, ...] == ['default', '...y', 'monokai']
E             
E             At index 0 diff: 'auto' != 'default'
E             Left contains 5 more items, first extra item: 'monokai'
E             Use -v to get more diff

httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_get_available_styles_1_test_valid_case.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_output_formatters_colors_get_available_styles_1_test_valid_case.py::test_get_available_styles
============================== 1 failed in 0.19s ===============================
"""