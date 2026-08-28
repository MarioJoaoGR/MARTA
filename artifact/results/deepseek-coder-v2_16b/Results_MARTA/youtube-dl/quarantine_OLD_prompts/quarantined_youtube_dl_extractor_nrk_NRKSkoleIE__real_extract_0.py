
import pytest
from unittest.mock import patch
from youtube_dl.extractor.nrk import NRKSkoleIE

class TestNRKSkoleIE:
    @patch('youtube_dl.extractor.nrk.NRKSkoleIE._download_json', return_value={'psId': '6021'})
    def test_valid_input(self, mock_download_json):
        nrk_ie = NRKSkoleIE()
        info_dict = nrk_ie._real_extract('https://www.nrk.no/skole/?page=search&q=&mediaId=14099')
        assert info_dict == {'url': 'nrk:6021', 'id': '6021', 'ext': 'mp4', 'title': None, 'description': None, 'duration': None}
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKSkoleIE__real_extract_0.py F [100%]

=================================== FAILURES ===================================
_______________________ TestNRKSkoleIE.test_valid_input ________________________

self = <test_youtube_dl_extractor_nrk_NRKSkoleIE__real_extract_0.TestNRKSkoleIE object at 0x7f8ca5497c70>
mock_download_json = <MagicMock name='_download_json' id='140242045205904'>

    @patch('youtube_dl.extractor.nrk.NRKSkoleIE._download_json', return_value={'psId': '6021'})
    def test_valid_input(self, mock_download_json):
        nrk_ie = NRKSkoleIE()
        info_dict = nrk_ie._real_extract('https://www.nrk.no/skole/?page=search&q=&mediaId=14099')
>       assert info_dict == {'url': 'nrk:6021', 'id': '6021', 'ext': 'mp4', 'title': None, 'description': None, 'duration': None}
E       AssertionError: assert {'_type': 'ur...': 'nrk:6021'} == {'description...: '6021', ...}
E         
E         Omitting 1 identical items, use -vv to show
E         Left contains 2 more items:
E         {'_type': 'url', 'ie_key': None}
E         Right contains 5 more items:
E         {'description': None,
E          'duration': None,...
E         
E         ...Full output truncated (4 lines hidden), use '-vv' to show

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKSkoleIE__real_extract_0.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKSkoleIE__real_extract_0.py::TestNRKSkoleIE::test_valid_input
============================== 1 failed in 0.72s ===============================
"""