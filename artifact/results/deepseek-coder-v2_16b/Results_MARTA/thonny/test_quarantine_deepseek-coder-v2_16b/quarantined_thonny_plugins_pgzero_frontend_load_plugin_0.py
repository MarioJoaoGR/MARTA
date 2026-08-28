
import pytest
from unittest.mock import patch, MagicMock
from thonny.plugins.pgzero_frontend import load_plugin, get_workbench, _OPTION_NAME, update_environment


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_plugins_pgzero_frontend_load_plugin_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_load_plugin _______________________________

mock_get_workbench = <MagicMock name='get_workbench' id='139882649363088'>

    @patch('thonny.plugins.pgzero_frontend.get_workbench')
    def test_load_plugin(mock_get_workbench):
        # Create a mock workbench object
        mock_workbench = MagicMock()
        mock_workbench.set_default.return_value = False
        mock_get_workbench.return_value = mock_workbench
    
        # Call the load_plugin function
        load_plugin()
    
        # Assert that set_default was called with the correct arguments
>       assert mock_get_workbench.call_count == 1
E       AssertionError: assert 3 == 1
E        +  where 3 = <MagicMock name='get_workbench' id='139882649363088'>.call_count

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_plugins_pgzero_frontend_load_plugin_0.py:17: AssertionError
____________________ test_load_plugin_with_existing_option _____________________

mock_get_workbench = <MagicMock name='get_workbench' id='139882649795552'>

    @patch('thonny.plugins.pgzero_frontend.get_workbench')
    def test_load_plugin_with_existing_option(mock_get_workbench):
        # Create a mock workbench object with the _OPTION_NAME already set to False
        mock_workbench = MagicMock()
        mock_workbench.set_default.return_value = False
        mock_workbench.add_command.return_value = None
        mock_get_workbench.return_value = mock_workbench
    
        # Call the load_plugin function
        load_plugin()
    
        # Assert that set_default was called with the correct arguments
>       assert mock_get_workbench.call_count == 1
E       AssertionError: assert 3 == 1
E        +  where 3 = <MagicMock name='get_workbench' id='139882649795552'>.call_count

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_plugins_pgzero_frontend_load_plugin_0.py:43: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_plugins_pgzero_frontend_load_plugin_0.py::test_load_plugin
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_plugins_pgzero_frontend_load_plugin_0.py::test_load_plugin_with_existing_option
============================== 2 failed in 0.05s ===============================
"""