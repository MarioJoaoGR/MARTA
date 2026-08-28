
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
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader__report_progress_status_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________ test_file_downloader_add_progress_hook ____________________

    def test_file_downloader_add_progress_hook():
        ydl = MagicMock()
        params = {}
        downloader = FileDownloader(ydl, params)
>       assert not hasattr(downloader, 'report_progress')
E       AssertionError: assert not True
E        +  where True = hasattr(<youtube_dl.downloader.common.FileDownloader object at 0x7f5f9dd59ff0>, 'report_progress')

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader__report_progress_status_0.py:10: AssertionError
_________________ test_file_downloader_report_progress_default _________________

    def test_file_downloader_report_progress_default():
        ydl = MagicMock()
        params = {}
        downloader = FileDownloader(ydl, params)
        with pytest.raises(AttributeError):
>           assert not hasattr(downloader, 'report_progress')
E           AssertionError: assert not True
E            +  where True = hasattr(<youtube_dl.downloader.common.FileDownloader object at 0x7f5f9ddd49d0>, 'report_progress')

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader__report_progress_status_0.py:17: AssertionError
_________________ test_file_downloader_report_progress_custom __________________

    def test_file_downloader_report_progress_custom():
        ydl = MagicMock()
        params = {'verbose': True}
        downloader = FileDownloader(ydl, params)
        with pytest.raises(AttributeError):
>           assert not hasattr(downloader, 'report_progress')
E           AssertionError: assert not True
E            +  where True = hasattr(<youtube_dl.downloader.common.FileDownloader object at 0x7f5f9ddd63e0>, 'report_progress')

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader__report_progress_status_0.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader__report_progress_status_0.py::test_file_downloader_add_progress_hook
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader__report_progress_status_0.py::test_file_downloader_report_progress_default
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader__report_progress_status_0.py::test_file_downloader_report_progress_custom
============================== 3 failed in 0.56s ===============================
"""