
import pytest
from unittest.mock import patch
from youtube_dl.extractor.tudou import TudouPlaylistIE

class TestTudouPlaylistIE:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.ie = TudouPlaylistIE()
    
    def test_valid_case(self):
        url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
        
        with patch('youtube_dl.extractor.tudou.TudouPlaylistIE._download_json', return_value={'items': [{'icode': 'video123', 'kw': 'Video Title 1'}, {'icode': 'video456', 'kw': 'Video Title 2'}]}):
            info_dict = self.ie._real_extract(url)
            assert info_dict['id'] == 'zzdE77v6Mmo'
            assert len(info_dict['entries']) == 2
            assert all('http://www.tudou.com/programs/view/video123' in entry['url'] for entry in info_dict['entries'])
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tudou_TudouPlaylistIE__real_extract_0.py F [100%]

=================================== FAILURES ===================================
_____________________ TestTudouPlaylistIE.test_valid_case ______________________

self = <test_youtube_dl_extractor_tudou_TudouPlaylistIE__real_extract_0.TestTudouPlaylistIE object at 0x7f3c1291eaa0>

    def test_valid_case(self):
        url = 'http://www.tudou.com/listplay/zzdE77v6Mmo.html'
    
        with patch('youtube_dl.extractor.tudou.TudouPlaylistIE._download_json', return_value={'items': [{'icode': 'video123', 'kw': 'Video Title 1'}, {'icode': 'video456', 'kw': 'Video Title 2'}]}):
            info_dict = self.ie._real_extract(url)
            assert info_dict['id'] == 'zzdE77v6Mmo'
            assert len(info_dict['entries']) == 2
>           assert all('http://www.tudou.com/programs/view/video123' in entry['url'] for entry in info_dict['entries'])
E           assert False
E            +  where False = all(<generator object TestTudouPlaylistIE.test_valid_case.<locals>.<genexpr> at 0x7f3c1292b840>)

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tudou_TudouPlaylistIE__real_extract_0.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tudou_TudouPlaylistIE__real_extract_0.py::TestTudouPlaylistIE::test_valid_case
============================== 1 failed in 0.64s ===============================
"""