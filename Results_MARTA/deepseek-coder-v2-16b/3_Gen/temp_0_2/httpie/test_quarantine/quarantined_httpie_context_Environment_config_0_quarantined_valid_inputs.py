
import pytest
from unittest.mock import patch, MagicMock
from httpie.context import Config, Environment

@pytest.fixture
def environment():
    return Environment()

def test_config_loads_existing_config(environment):
    with patch('httpie.context.Config', autospec=True) as mock_config:
        # Mock the Config object to simulate an existing config file
        mock_config_instance = mock_config.return_value
        mock_config_instance.is_new.return_value = False
        mock_config_instance.load.side_effect = None  # No exception for load()

        # Call the method under test
        config = environment.config()
        
        assert isinstance(config, Config)

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_context_Environment_config_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________ test_config_loads_existing_config _______________________

environment = <Environment {'apply_warnings_filter': <function Environment.apply_warnings_filter at 0x7f51a90d91c0>,
 'args': Namesp...IO name=6 mode='rb+' closefd=True>" mode='r+' encoding='utf-8'>,
 'stdout_encoding': 'utf-8',
 'stdout_isatty': False}>

    def test_config_loads_existing_config(environment):
        with patch('httpie.context.Config', autospec=True) as mock_config:
            # Mock the Config object to simulate an existing config file
            mock_config_instance = mock_config.return_value
            mock_config_instance.is_new.return_value = False
            mock_config_instance.load.side_effect = None  # No exception for load()
    
            # Call the method under test
>           config = environment.config()
E           TypeError: 'NonCallableMagicMock' object is not callable

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_context_Environment_config_0_test_valid_inputs.py:18: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_context_Environment_config_0_test_valid_inputs.py::test_config_loads_existing_config
============================== 1 failed in 0.14s ===============================
"""