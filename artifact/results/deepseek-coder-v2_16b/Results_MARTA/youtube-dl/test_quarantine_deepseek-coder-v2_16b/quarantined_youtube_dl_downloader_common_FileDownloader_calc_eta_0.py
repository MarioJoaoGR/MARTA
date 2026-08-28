
import pytest
from youtube_dl.downloader.common import FileDownloader




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_calc_eta_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
________________________ test_calc_eta_with_none_total _________________________

    def test_calc_eta_with_none_total():
>       start = time.time()
E       NameError: name 'time' is not defined

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_calc_eta_0.py:6: NameError
_______________________ test_calc_eta_with_zero_current ________________________

    def test_calc_eta_with_zero_current():
>       start = time.time()
E       NameError: name 'time' is not defined

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_calc_eta_0.py:11: NameError
_________________________ test_calc_eta_with_small_dif _________________________

    def test_calc_eta_with_small_dif():
>       start = time.time()
E       NameError: name 'time' is not defined

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_calc_eta_0.py:16: NameError
________________________ test_calc_eta_with_valid_rate _________________________

    def test_calc_eta_with_valid_rate():
>       start = time.time()
E       NameError: name 'time' is not defined

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_calc_eta_0.py:21: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_calc_eta_0.py::test_calc_eta_with_none_total
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_calc_eta_0.py::test_calc_eta_with_zero_current
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_calc_eta_0.py::test_calc_eta_with_small_dif
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_calc_eta_0.py::test_calc_eta_with_valid_rate
============================== 4 failed in 0.56s ===============================
"""