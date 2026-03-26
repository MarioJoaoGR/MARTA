
from isort.settings import Config
import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_config():
    return MagicMock(spec=Config)

def test_valid_case(mock_config):
    # Create a mock instance of Config
    config = mock_config.return_value
    
    # Set the supported extensions and blocked extensions for the mock Config instance
    config.supported_extensions = ['.py']
    config.blocked_extensions = []
    
    # Test a valid file with .py extension
    assert config.is_supported_filetype('valid_script.py') is True

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

isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_0_test_valid_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

mock_config = <MagicMock spec='Config' id='139710113330384'>

    def test_valid_case(mock_config):
        # Create a mock instance of Config
        config = mock_config.return_value
    
        # Set the supported extensions and blocked extensions for the mock Config instance
        config.supported_extensions = ['.py']
        config.blocked_extensions = []
    
        # Test a valid file with .py extension
>       assert config.is_supported_filetype('valid_script.py') is True
E       AssertionError: assert <MagicMock name='mock().is_supported_filetype()' id='139710113194832'> is True
E        +  where <MagicMock name='mock().is_supported_filetype()' id='139710113194832'> = <MagicMock name='mock().is_supported_filetype' id='139710113188368'>('valid_script.py')
E        +    where <MagicMock name='mock().is_supported_filetype' id='139710113188368'> = <MagicMock name='mock()' id='139710132983184'>.is_supported_filetype

isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_0_test_valid_case.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_settings_Config_is_supported_filetype_0_test_valid_case.py::test_valid_case
============================== 1 failed in 0.10s ===============================
"""