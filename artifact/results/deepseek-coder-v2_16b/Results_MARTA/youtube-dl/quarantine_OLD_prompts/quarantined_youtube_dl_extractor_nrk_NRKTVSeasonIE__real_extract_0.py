
import pytest
from unittest.mock import patch
from youtube_dl.extractor.nrk import NRKTVSeasonIE


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVSeasonIE__real_extract_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_valid_case_1 _______________________________

    def test_valid_case_1():
        with patch('youtube_dl.extractor.nrk.NRKTVSeasonIE._call_api', return_value={'titles': {'title': 'Sesong 1'}}):
            nrk_season_extractor = NRKTVSeasonIE()
            info_dict = nrk_season_extractor._real_extract('https://tv.nrk.no/serie/backstage/sesong/1')
>           assert info_dict == {'id': 'backstage/1', 'title': 'Sesong 1'}
E           AssertionError: assert {'_type': 'pl...': 'Sesong 1'} == {'id': 'backs...': 'Sesong 1'}
E             
E             Omitting 2 identical items, use -vv to show
E             Left contains 2 more items:
E             {'_type': 'playlist',
E              'entries': <generator object NRKTVSerieBaseIE._entries at 0x7f92be8f3d80>}
E             Use -v to get more diff

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVSeasonIE__real_extract_0.py:10: AssertionError
______________________________ test_valid_case_2 _______________________________

    def test_valid_case_2():
        with patch('youtube_dl.extractor.nrk.NRKTVSeasonIE._call_api', return_value={'titles': {'title': 'Sesong 1'}}):
            nrk_season_extractor = NRKTVSeasonIE()
            info_dict = nrk_season_extractor._real_extract('https://radio.nrk.no/serie/dickie-dick-dickens/sesong/1')
>           assert info_dict == {'id': 'dickie-dick-dickens/1', 'title': 'Sesong 1'}
E           AssertionError: assert {'_type': 'pl...': 'Sesong 1'} == {'id': 'dicki...': 'Sesong 1'}
E             
E             Omitting 2 identical items, use -vv to show
E             Left contains 2 more items:
E             {'_type': 'playlist',
E              'entries': <generator object NRKTVSerieBaseIE._entries at 0x7f92be7725e0>}
E             Use -v to get more diff

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVSeasonIE__real_extract_0.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVSeasonIE__real_extract_0.py::test_valid_case_1
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVSeasonIE__real_extract_0.py::test_valid_case_2
============================== 2 failed in 0.58s ===============================
"""