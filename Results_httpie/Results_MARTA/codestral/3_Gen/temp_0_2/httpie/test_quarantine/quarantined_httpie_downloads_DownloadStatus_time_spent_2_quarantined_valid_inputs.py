
import pytest
from datetime import datetime, timedelta
from unittest.mock import patch
from httpie.downloads import DownloadStatus

@pytest.fixture
def setup():
    env = "network_storage"
    download_status = DownloadStatus(env)
    download_status.downloaded = 1024
    download_status.total_size = 102400
    download_status.resumed_from = 0
    now = datetime.now()
    download_status.time_started = now
    
    # Mock the time finishing after 60 seconds
    with patch('httpie.downloads.DownloadStatus.time_finished', new=now + timedelta(seconds=60)):
        yield download_status

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
============================ no tests ran in 0.18s =============================
"""