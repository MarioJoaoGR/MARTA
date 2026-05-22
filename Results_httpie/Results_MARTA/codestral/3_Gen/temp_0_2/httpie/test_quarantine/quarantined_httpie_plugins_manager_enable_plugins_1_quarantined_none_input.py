
from pathlib import Path
from contextlib import nullcontext
from httpie.plugins.manager import enable_plugins
from unittest.mock import patch, MagicMock
import pytest

@pytest.mark.parametrize("plugins_dir", [None, Path("/path/to/plugins")])
def test_none_input(plugins_dir):
    with patch('httpie.plugins.manager.enable_plugins') as mock_enable_plugins:
        enable_plugins(plugins_dir)
        if plugins_dir is None:
            assert isinstance(mock_enable_plugins.return_value, nullcontext)
        else:
            # Add more assertions here to verify the behavior when a valid plugins_dir is provided
            pass

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_enable_plugins_1_test_none_input.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_none_input[None] _____________________________

plugins_dir = None

    @pytest.mark.parametrize("plugins_dir", [None, Path("/path/to/plugins")])
    def test_none_input(plugins_dir):
        with patch('httpie.plugins.manager.enable_plugins') as mock_enable_plugins:
            enable_plugins(plugins_dir)
            if plugins_dir is None:
>               assert isinstance(mock_enable_plugins.return_value, nullcontext)
E               AssertionError: assert False
E                +  where False = isinstance(<MagicMock name='enable_plugins()' id='139749464324880'>, nullcontext)
E                +    where <MagicMock name='enable_plugins()' id='139749464324880'> = <MagicMock name='enable_plugins' id='139749444773520'>.return_value

httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_enable_plugins_1_test_none_input.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_enable_plugins_1_test_none_input.py::test_none_input[None]
========================= 1 failed, 1 passed in 0.21s ==========================
"""