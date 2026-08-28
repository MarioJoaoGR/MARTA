
import pytest
from unittest.mock import MagicMock
from youtube_dl.downloader.common import FileDownloader


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_report_retry_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

    def test_edge_case():
        ydl = MagicMock()
        params = {}
        downloader = FileDownloader(ydl, params)
        default_params = {
            'buffersize': 32768,
            'continuedl': False,
            'consoletitle': False,
            'external_downloader_args': [],
            'hls_use_mpegts': False,
            'http_chunk_size': None,
        }
>       assert downloader.params == default_params, f"Expected {default_params}, but got {downloader.params}"
E       AssertionError: Expected {'buffersize': 32768, 'continuedl': False, 'consoletitle': False, 'external_downloader_args': [], 'hls_use_mpegts': False, 'http_chunk_size': None}, but got {}
E       assert {} == {'buffersize'...rgs': [], ...}
E         
E         Right contains 6 more items:
E         {'buffersize': 32768,
E          'consoletitle': False,
E          'continuedl': False,
E          'external_downloader_args': [],
E          'hls_use_mpegts': False,
E          'http_chunk_size': None}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_report_retry_0.py:18: AssertionError
_______________________________ test_error_case ________________________________

    def test_error_case():
        ydl = MagicMock()
        params = {'verbose': 'True', 'ratelimit': 10240, 'retries': 3, 'buffersize': 8192, 'test': False}
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_report_retry_0.py:23: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_report_retry_0.py::test_edge_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_report_retry_0.py::test_error_case
============================== 2 failed in 0.70s ===============================
"""