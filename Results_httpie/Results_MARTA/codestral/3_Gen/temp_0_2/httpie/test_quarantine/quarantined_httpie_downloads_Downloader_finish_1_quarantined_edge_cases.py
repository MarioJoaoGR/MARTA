
import pytest
from unittest.mock import patch, MagicMock
from httpie.downloads import Downloader, Environment, DownloadStatus

@pytest.fixture
def setup_downloader():
    env = Environment(config={"network": "example.com"})
    output_file = MagicMock()
    downloader = Downloader(env=env, output_file=output_file, resume=False)
    return downloader

@pytest.mark.parametrize("finished", [False])
def test_finish(setup_downloader):
    downloader = setup_downloader
    with patch('httpie.downloads.DownloadStatus.finished', new_callable=MagicMock) as mock_status:
        assert not downloader.finished
        downloader.finish()
        assert downloader.finished
        mock_status.assert_called_once()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests_codestral/test_httpie_downloads_Downloader_finish_1_test_edge_cases.py _
In test_finish: function uses no argument 'finished'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_codestral/test_httpie_downloads_Downloader_finish_1_test_edge_cases.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.26s ===============================
"""