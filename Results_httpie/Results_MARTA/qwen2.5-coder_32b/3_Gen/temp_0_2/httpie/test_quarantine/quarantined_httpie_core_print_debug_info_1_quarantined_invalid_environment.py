
import pytest
from unittest.mock import patch, MagicMock
from httpie.core import print_debug_info
from httpie import __version__ as httpie_version
from requests import __version__ as requests_version
from pygments import __version__ as pygments_version
import sys
import platform

@pytest.fixture
def mock_environment():
    env = MagicMock()
    return env

def test_invalid_environment(mock_environment):
    with pytest.raises(AttributeError):
        print_debug_info(mock_environment)

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_core_print_debug_info_1_test_invalid_environment.py F [100%]

=================================== FAILURES ===================================
___________________________ test_invalid_environment ___________________________

mock_environment = <MagicMock id='139893055364368'>

    def test_invalid_environment(mock_environment):
>       with pytest.raises(AttributeError):
E       Failed: DID NOT RAISE <class 'AttributeError'>

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_core_print_debug_info_1_test_invalid_environment.py:17: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_core_print_debug_info_1_test_invalid_environment.py::test_invalid_environment
============================== 1 failed in 0.24s ===============================
"""