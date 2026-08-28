
import pytest
from youtube_dl.extractor.nrk import NRKTVEpisodeIE

# Test for valid case

# Test for edge case where season number is invalid
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVEpisodeIE__real_extract_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        extractor = NRKTVEpisodeIE()
        url = 'https://tv.nrk.no/serie/hellums-kro/sesong/1/episode/2'
>       info_dict = extractor._real_extract(url)

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVEpisodeIE__real_extract_0.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/nrk.py:457: in _real_extract
    webpage = self._download_webpage(url, display_id)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:798: in _download_webpage
    res = self._download_webpage_handle(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:667: in _download_webpage_handle
    urlh = self._request_webpage(url_or_request, video_id, note, errnote, fatal, data=data, headers=headers, query=query, expected_status=expected_status)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:606: in _request_webpage
    self.report_download_webpage(video_id)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:929: in report_download_webpage
    self.to_screen('%s: Downloading webpage' % video_id)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <youtube_dl.extractor.nrk.NRKTVEpisodeIE object at 0x7fb76fc438b0>
msg = 'hellums-kro/sesong/1/episode/2: Downloading webpage'

    def to_screen(self, msg):
        """Print msg to screen, prefixing it with '[ie_name]'"""
>       self._downloader.to_screen('[%s] %s' % (self.IE_NAME, msg))
E       AttributeError: 'NoneType' object has no attribute 'to_screen'

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:921: AttributeError
________________________________ test_edge_case ________________________________

    def test_edge_case():
        extractor = NRKTVEpisodeIE()
        url = 'https://tv.nrk.no/serie/hellums-kro/sesong/100/episode/2'
        with pytest.raises(Exception) as e:
            info_dict = extractor._real_extract(url)
>       assert str(e.value) == "ProgramRightsHasExpired"
E       assert "'NoneType' o...e 'to_screen'" == 'ProgramRightsHasExpired'
E         
E         - ProgramRightsHasExpired
E         + 'NoneType' object has no attribute 'to_screen'

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVEpisodeIE__real_extract_0.py:27: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVEpisodeIE__real_extract_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKTVEpisodeIE__real_extract_0.py::test_edge_case
============================== 2 failed in 0.66s ===============================
"""