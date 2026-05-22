
import pytest
from unittest.mock import patch
from httpie.downloads import DownloadStatus

def test_edge_case():
    download_status = DownloadStatus(env="test_env")
    with patch('builtins.hasattr', return_value=False):
        with patch('time.monotonic', return_value=123456.789):
            download_status.time_started = 123456.789
            download_status.finished()
            assert download_status.time_finished == pytest.approx(123456.789, abs=0.001)

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_DownloadStatus_finished_0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        download_status = DownloadStatus(env="test_env")
        with patch('builtins.hasattr', return_value=False):
            with patch('time.monotonic', return_value=123456.789):
                download_status.time_started = 123456.789
                download_status.finished()
>               assert download_status.time_finished == pytest.approx(123456.789, abs=0.001)
E               assert 1139517.335528447 == 123456.789 ± 1.0e-03
E                 
E                 comparison failed
E                 Obtained: 1139517.335528447
E                 Expected: 123456.789 ± 1.0e-03

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_DownloadStatus_finished_0_test_edge_case.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_DownloadStatus_finished_0_test_edge_case.py::test_edge_case
============================== 1 failed in 0.18s ===============================
"""