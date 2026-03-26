
import pytest
import logging
from pytutils.log import configure, DEFAULT_CONFIG

# Assuming DEFAULT_CONFIG is defined somewhere in the module or can be imported directly

def test_configure_with_direct_input():
    """Test configuring with a direct input configuration."""
    log = logging.getLogger(__name__)
    config = {'handlers': [{'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'simple'}]}
    configure(config=config)
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

pytutils/Test4DT_tests/test_pytutils_log_configure_0.py F                [100%]

=================================== FAILURES ===================================
_______________________ test_configure_with_direct_input _______________________

    def test_configure_with_direct_input():
        """Test configuring with a direct input configuration."""
        log = logging.getLogger(__name__)
        config = {'handlers': [{'level': 'DEBUG', 'class': 'logging.StreamHandler', 'formatter': 'simple'}]}
>       configure(config=config)

pytutils/Test4DT_tests/test_pytutils_log_configure_0.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/log.py:96: in configure
    logging.config.dictConfig(cfg)
/usr/local/lib/python3.11/logging/config.py:823: in dictConfig
    dictConfigClass(config).configure()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <logging.config.DictConfigurator object at 0x7f2b3c1a5fd0>

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
FAILED pytutils/Test4DT_tests/test_pytutils_log_configure_0.py::test_configure_with_direct_input
============================== 1 failed in 0.09s ===============================
"""