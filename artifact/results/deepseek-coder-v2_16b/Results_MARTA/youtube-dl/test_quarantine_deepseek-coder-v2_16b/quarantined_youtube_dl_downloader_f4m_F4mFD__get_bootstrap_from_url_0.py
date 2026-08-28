
import pytest
from youtube_dl import YoutubeDL
from youtube_dl.downloader.f4m import F4mFD



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_F4mFD__get_bootstrap_from_url_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_valid_bootstrap_download _________________________

    def test_valid_bootstrap_download():
        ydl = YoutubeDL()
>       f4m_fd = F4mFD(ydl)
E       TypeError: FileDownloader.__init__() missing 1 required positional argument: 'params'

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_F4mFD__get_bootstrap_from_url_0.py:8: TypeError
_______________________________ test_invalid_url _______________________________

    def test_invalid_url():
        ydl = YoutubeDL()
>       f4m_fd = F4mFD(ydl)
E       TypeError: FileDownloader.__init__() missing 1 required positional argument: 'params'

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_F4mFD__get_bootstrap_from_url_0.py:17: TypeError
_________________________ test_missing_lines_to_cover __________________________

    def test_missing_lines_to_cover():
        ydl = YoutubeDL()
>       f4m_fd = F4mFD(ydl)
E       TypeError: FileDownloader.__init__() missing 1 required positional argument: 'params'

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_F4mFD__get_bootstrap_from_url_0.py:23: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_F4mFD__get_bootstrap_from_url_0.py::test_valid_bootstrap_download
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_F4mFD__get_bootstrap_from_url_0.py::test_invalid_url
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_f4m_F4mFD__get_bootstrap_from_url_0.py::test_missing_lines_to_cover
============================== 3 failed in 0.59s ===============================
"""