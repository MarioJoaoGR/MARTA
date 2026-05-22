
from httpie.config import BaseConfigDict
from pathlib import Path
import pytest
from unittest.mock import patch

def test_valid_input():
    with patch('httpie.config.BaseConfigDict.__init__', return_value=None):
        config = BaseConfigDict(path=Path('/some/file/path'))
        assert hasattr(config, 'path')

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

httpie/Test4DT_tests_codestral/test_httpie_config_BaseConfigDict_pre_process_data_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        with patch('httpie.config.BaseConfigDict.__init__', return_value=None):
            config = BaseConfigDict(path=Path('/some/file/path'))
>           assert hasattr(config, 'path')
E           AssertionError: assert False
E            +  where False = hasattr({}, 'path')

httpie/Test4DT_tests_codestral/test_httpie_config_BaseConfigDict_pre_process_data_0_test_valid_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_config_BaseConfigDict_pre_process_data_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.07s ===============================
"""