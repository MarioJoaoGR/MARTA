
import pytest
from datetime import datetime, timedelta
from unittest.mock import patch
from httpie.downloads import DownloadStatus

@pytest.fixture
def setup():
    return DownloadStatus(env="test_environment")

def test_time_spent(setup):
    with patch('httpie.downloads.DownloadStatus.time_started', create=True, new=datetime.now()):
        with patch('httpie.downloads.DownloadStatus.time_finished', create=True, new=datetime.now() + timedelta(seconds=60)):
            assert setup.time_spent().total_seconds() == 60

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

httpie/Test4DT_tests_codestral/test_httpie_downloads_DownloadStatus_time_spent_3_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_time_spent ________________________________

setup = <httpie.downloads.DownloadStatus object at 0x7f846700b790>

    def test_time_spent(setup):
        with patch('httpie.downloads.DownloadStatus.time_started', create=True, new=datetime.now()):
            with patch('httpie.downloads.DownloadStatus.time_finished', create=True, new=datetime.now() + timedelta(seconds=60)):
>               assert setup.time_spent().total_seconds() == 60
E               TypeError: 'NoneType' object is not callable

httpie/Test4DT_tests_codestral/test_httpie_downloads_DownloadStatus_time_spent_3_test_valid_inputs.py:14: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_downloads_DownloadStatus_time_spent_3_test_valid_inputs.py::test_time_spent
============================== 1 failed in 0.24s ===============================
"""