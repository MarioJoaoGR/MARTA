
import logging
from unittest.mock import patch
from pytutils.log import get_config, configure, DEFAULT_CONFIG

def test_valid_inputs():
    with patch('pytutils.log.get_config') as mock_get_config:
        # Mock the return value of get_config to simulate valid configuration
        mock_get_config.return_value = {'logging': {'level': 'DEBUG'}}
    
        log = logging.getLogger(__name__)
        configure()
        
        assert log.getEffectiveLevel() == logging.DEBUG, "Expected DEBUG level but got something else"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_log_configure_0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        with patch('pytutils.log.get_config') as mock_get_config:
            # Mock the return value of get_config to simulate valid configuration
            mock_get_config.return_value = {'logging': {'level': 'DEBUG'}}
    
            log = logging.getLogger(__name__)
>           configure()

pytutils/Test4DT_tests/test_pytutils_log_configure_0_test_valid_inputs.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/log.py:96: in configure
    logging.config.dictConfig(cfg)
/usr/local/lib/python3.11/logging/config.py:823: in dictConfig
    dictConfigClass(config).configure()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <logging.config.DictConfigurator object at 0x7fc847448c50>

    def configure(self):
        """Do the configuration."""
    
        config = self.config
        if 'version' not in config:
>           raise ValueError("dictionary doesn't specify a version")
E           ValueError: dictionary doesn't specify a version

/usr/local/lib/python3.11/logging/config.py:506: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_log_configure_0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.07s ===============================
"""