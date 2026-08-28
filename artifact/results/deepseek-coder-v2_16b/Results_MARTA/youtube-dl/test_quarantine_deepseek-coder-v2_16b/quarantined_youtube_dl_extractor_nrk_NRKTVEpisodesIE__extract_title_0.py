
import pytest
from youtube_dl.extractor.nrk import NRKTVEpisodesIE


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVEpisodesIE__extract_title_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        nrk_ie = NRKTVEpisodesIE()
        url = 'https://tv.nrk.no/program/episodes/nytt-paa-nytt/69031'
>       info_dict = nrk_ie.extract_info(url)
E       AttributeError: 'NRKTVEpisodesIE' object has no attribute 'extract_info'

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVEpisodesIE__extract_title_0.py:8: AttributeError
_____________________________ test_nonexistent_url _____________________________

    def test_nonexistent_url():
        nrk_ie = NRKTVEpisodesIE()
        url = 'https://example.com/invalid-url'
>       info_dict = nrk_ie.extract_info(url)
E       AttributeError: 'NRKTVEpisodesIE' object has no attribute 'extract_info'

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVEpisodesIE__extract_title_0.py:18: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVEpisodesIE__extract_title_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVEpisodesIE__extract_title_0.py::test_nonexistent_url
============================== 2 failed in 0.57s ===============================
"""