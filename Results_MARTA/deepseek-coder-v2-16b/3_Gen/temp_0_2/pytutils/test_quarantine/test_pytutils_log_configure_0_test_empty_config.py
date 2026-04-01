
import pytest
import logging
from pytutils.log import configure, DEFAULT_CONFIG

@pytest.fixture(autouse=True)
def setup():
    # Reset logging configuration before each test
    logging.config.dictConfig({})

def test_empty_config():
    log = logging.getLogger(__name__)
    configure()
    log.info('test')  # Check if the basic configuration is applied correctly

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

pytutils/Test4DT_tests/test_pytutils_log_configure_0_test_empty_config.py E [100%]

==================================== ERRORS ====================================
_____________________ ERROR at setup of test_empty_config ______________________

    @pytest.fixture(autouse=True)
    def setup():
        # Reset logging configuration before each test
>       logging.config.dictConfig({})

pytutils/Test4DT_tests/test_pytutils_log_configure_0_test_empty_config.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/logging/config.py:823: in dictConfig
    dictConfigClass(config).configure()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <logging.config.DictConfigurator object at 0x7f6ccdb53610>

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
ERROR pytutils/Test4DT_tests/test_pytutils_log_configure_0_test_empty_config.py::test_empty_config
=============================== 1 error in 0.07s ===============================
"""