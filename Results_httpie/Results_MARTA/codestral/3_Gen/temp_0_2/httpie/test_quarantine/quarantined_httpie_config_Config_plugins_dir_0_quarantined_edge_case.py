
import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from httpie.config import Config, DEFAULT_CONFIG_DIR

@pytest.fixture
def config():
    return Config()

def test_plugins_dir(config):
    with patch('httpie.config.Path', spec=Path) as mock_path:
        # Mock the default directory to be a specific path for testing
        mock_default_dir = MagicMock(spec=Path)
        mock_default_dir.__str__.return_value = DEFAULT_CONFIG_DIR
    
        with patch('httpie.config.DEFAULT_CONFIG_DIR', new=mock_default_dir):
            # Test the plugins_dir method
            assert config.plugins_dir() == Path(DEFAULT_CONFIG_DIR) / 'plugins'

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

httpie/Test4DT_tests_codestral/test_httpie_config_Config_plugins_dir_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_plugins_dir _______________________________

config = {'default_options': []}

    def test_plugins_dir(config):
        with patch('httpie.config.Path', spec=Path) as mock_path:
            # Mock the default directory to be a specific path for testing
            mock_default_dir = MagicMock(spec=Path)
            mock_default_dir.__str__.return_value = DEFAULT_CONFIG_DIR
    
            with patch('httpie.config.DEFAULT_CONFIG_DIR', new=mock_default_dir):
                # Test the plugins_dir method
>               assert config.plugins_dir() == Path(DEFAULT_CONFIG_DIR) / 'plugins'
E               AssertionError: assert <MagicMock name='Path().expanduser().resolve()()' id='140050161287632'> == (PosixPath('/home/joaovitorino/.config/httpie') / 'plugins')
E                +  where <MagicMock name='Path().expanduser().resolve()()' id='140050161287632'> = <MagicMock name='Path().expanduser().resolve()' id='140050177943312'>()
E                +    where <MagicMock name='Path().expanduser().resolve()' id='140050177943312'> = {'default_options': []}.plugins_dir
E                +  and   PosixPath('/home/joaovitorino/.config/httpie') = Path(PosixPath('/home/joaovitorino/.config/httpie'))

httpie/Test4DT_tests_codestral/test_httpie_config_Config_plugins_dir_0_test_edge_case.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_config_Config_plugins_dir_0_test_edge_case.py::test_plugins_dir
============================== 1 failed in 0.16s ===============================
"""