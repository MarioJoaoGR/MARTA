
import pytest
from youtube_dl.extractor.nrk import NRKIE

# Test for valid TV episode URL

# Test for error case radio program URL
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVIE__real_extract_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________________________ test_valid_case_tv_episode __________________________

    def test_valid_case_tv_episode():
        nrk_ie = NRKIE()
        url = 'https://tv.nrk.no/program/MDDP12000117'
>       info_dict = nrk_ie._real_extract(url)

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVIE__real_extract_1.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/nrk.py:148: in _real_extract
    video_id = self._match_id(url).split('/')[-1]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'youtube_dl.extractor.nrk.NRKIE'>
url = 'https://tv.nrk.no/program/MDDP12000117'

    @classmethod
    def _match_id(cls, url):
        if '_VALID_URL_RE' not in cls.__dict__:
            cls._VALID_URL_RE = re.compile(cls._VALID_URL)
        m = cls._VALID_URL_RE.match(url)
>       assert m
E       AssertionError

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:422: AssertionError
________________________ test_error_case_radio_program _________________________

    def test_error_case_radio_program():
        nrk_ie = NRKIE()
        url = 'https://radio.nrk.no/serie/dagsnytt/NPUB21019315/12-07-2015#'
        with pytest.raises(ValueError):
>           nrk_ie._real_extract(url)

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVIE__real_extract_1.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/nrk.py:148: in _real_extract
    video_id = self._match_id(url).split('/')[-1]
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'youtube_dl.extractor.nrk.NRKIE'>
url = 'https://radio.nrk.no/serie/dagsnytt/NPUB21019315/12-07-2015#'

    @classmethod
    def _match_id(cls, url):
        if '_VALID_URL_RE' not in cls.__dict__:
            cls._VALID_URL_RE = re.compile(cls._VALID_URL)
        m = cls._VALID_URL_RE.match(url)
>       assert m
E       AssertionError

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:422: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVIE__real_extract_1.py::test_valid_case_tv_episode
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVIE__real_extract_1.py::test_error_case_radio_program
============================== 2 failed in 0.65s ===============================
"""