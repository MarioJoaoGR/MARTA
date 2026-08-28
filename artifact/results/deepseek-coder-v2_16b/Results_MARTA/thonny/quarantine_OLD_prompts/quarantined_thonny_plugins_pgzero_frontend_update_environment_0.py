
import pytest
from unittest.mock import patch, MagicMock
import os
from thonny.plugins.pgzero_frontend import get_workbench, _OPTION_NAME


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_plugins_pgzero_frontend_update_environment_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_____________________ test_update_environment_simple_mode ______________________

    def test_update_environment_simple_mode():
        with patch('thonny.plugins.pgzero_frontend.get_workbench') as mock_get_workbench:
            mock_get_workbench().in_simple_mode.return_value = True
>           update_environment()
E           NameError: name 'update_environment' is not defined

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_plugins_pgzero_frontend_update_environment_0.py:10: NameError
___________________ test_update_environment_not_simple_mode ____________________

    def test_update_environment_not_simple_mode():
        with patch('thonny.plugins.pgzero_frontend.get_workbench') as mock_get_workbench:
            mock_get_workbench().in_simple_mode.return_value = False
            mock_get_workbench().get_option.return_value = "some_option_value"
>           update_environment()
E           NameError: name 'update_environment' is not defined

/opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_plugins_pgzero_frontend_update_environment_0.py:17: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_plugins_pgzero_frontend_update_environment_0.py::test_update_environment_simple_mode
FAILED ../../../../../opt/marta/baselines/Results_MARTA/thonny/Test4DT_tests_deepseek-coder-v2_16b/test_thonny_plugins_pgzero_frontend_update_environment_0.py::test_update_environment_not_simple_mode
============================== 2 failed in 0.04s ===============================
"""