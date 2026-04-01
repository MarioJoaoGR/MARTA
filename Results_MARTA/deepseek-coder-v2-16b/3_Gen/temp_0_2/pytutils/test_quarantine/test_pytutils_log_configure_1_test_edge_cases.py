
import pytest
import logging
from pytutils.log import configure, DEFAULT_CONFIG, get_config

def test_edge_cases():
    log = logging.getLogger(__name__)
    
    # First call to configure without any parameters should use the default configuration
    configure()
    log.info('test')  # Should use the default configuration

    # Second call to configure with a specific config should override the default configuration
    config = {'handlers': [{'type': 'file', 'filename': 'app.log'}]}
    configure(config=config)
    log.info('test')  # Should now log to file instead of console

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

pytutils/Test4DT_tests/test_pytutils_log_configure_1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_edge_cases ________________________________

    def test_edge_cases():
        log = logging.getLogger(__name__)
    
        # First call to configure without any parameters should use the default configuration
        configure()
        log.info('test')  # Should use the default configuration
    
        # Second call to configure with a specific config should override the default configuration
        config = {'handlers': [{'type': 'file', 'filename': 'app.log'}]}
>       configure(config=config)

pytutils/Test4DT_tests/test_pytutils_log_configure_1_test_edge_cases.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/log.py:96: in configure
    logging.config.dictConfig(cfg)
/usr/local/lib/python3.11/logging/config.py:823: in dictConfig
    dictConfigClass(config).configure()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <logging.config.DictConfigurator object at 0x7f10f266b350>

    def configure(self):
        """Do the configuration."""
    
        config = self.config
        if 'version' not in config:
>           raise ValueError("dictionary doesn't specify a version")
E           ValueError: dictionary doesn't specify a version

/usr/local/lib/python3.11/logging/config.py:506: ValueError
----------------------------- Captured stderr call -----------------------------
[40m[32m[00:03:34] [Test4DT_tests.test_pytutils_log_configure_1_test_edge_cases/1021765] test [34m@test_edge_cases:11 #INFO[0m
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_log_configure_1_test_edge_cases.py::test_edge_cases
============================== 1 failed in 0.10s ===============================
"""