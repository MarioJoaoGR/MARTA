
import pytest
from youtube_dl.extractor.nrk import NRKSkoleIE

@pytest.fixture(scope="module")
def nrk_ie():
    return NRKSkoleIE()



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKSkoleIE__real_extract_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

nrk_ie = <youtube_dl.extractor.nrk.NRKSkoleIE object at 0x7ff8e3f17970>

    def test_valid_input(nrk_ie):
        url = 'https://www.nrk.no/skole/?page=search&q=&mediaId=14099'
>       info_dict = nrk_ie._real_extract(url)

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKSkoleIE__real_extract_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/nrk.py:869: in _real_extract
    nrk_id = self._download_json(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:895: in _download_json
    res = self._download_json_handle(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:874: in _download_json_handle
    res = self._download_webpage_handle(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:667: in _download_webpage_handle
    urlh = self._request_webpage(url_or_request, video_id, note, errnote, fatal, data=data, headers=headers, query=query, expected_status=expected_status)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:611: in _request_webpage
    self.to_screen('%s: %s' % (video_id, note))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <youtube_dl.extractor.nrk.NRKSkoleIE object at 0x7ff8e3f17970>
msg = '14099: Downloading JSON metadata'

    def to_screen(self, msg):
        """Print msg to screen, prefixing it with '[ie_name]'"""
>       self._downloader.to_screen('[%s] %s' % (self.IE_NAME, msg))
E       AttributeError: 'NoneType' object has no attribute 'to_screen'

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:921: AttributeError
______________________________ test_missing_lines ______________________________

nrk_ie = <youtube_dl.extractor.nrk.NRKSkoleIE object at 0x7ff8e3f17970>

    def test_missing_lines(nrk_ie):
        url = 'https://www.nrk.no/skole/?page=objectives&subject=naturfag&objective=K15114&mediaId=19355'
        with pytest.raises(Exception) as e:
            nrk_ie._real_extract(url)
>       assert str(e.value).startswith('Expected URL to match the pattern'), f"Expected exception for missing lines, but got {str(e.value)}"
E       AssertionError: Expected exception for missing lines, but got 'NoneType' object has no attribute 'to_screen'
E       assert False
E        +  where False = <built-in method startswith of str object at 0x7ff8e3de12f0>('Expected URL to match the pattern')
E        +    where <built-in method startswith of str object at 0x7ff8e3de12f0> = "'NoneType' object has no attribute 'to_screen'".startswith
E        +      where "'NoneType' object has no attribute 'to_screen'" = str(AttributeError("'NoneType' object has no attribute 'to_screen'"))
E        +        where AttributeError("'NoneType' object has no attribute 'to_screen'") = <ExceptionInfo AttributeError("'NoneType' object has no attribute 'to_screen'") tblen=7>.value

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKSkoleIE__real_extract_0.py:20: AssertionError
______________________________ test_invalid_input ______________________________

nrk_ie = <youtube_dl.extractor.nrk.NRKSkoleIE object at 0x7ff8e3f17970>

    def test_invalid_input(nrk_ie):
        url = 'invalid-url'
        with pytest.raises(Exception) as e:
            nrk_ie._real_extract(url)
>       assert str(e.value).startswith('Expected URL to match the pattern'), f"Expected exception for invalid input, but got {str(e.value)}"
E       AssertionError: Expected exception for invalid input, but got 
E       assert False
E        +  where False = <built-in method startswith of str object at 0x7ff8e6448030>('Expected URL to match the pattern')
E        +    where <built-in method startswith of str object at 0x7ff8e6448030> = ''.startswith
E        +      where '' = str(AssertionError())
E        +        where AssertionError() = <ExceptionInfo AssertionError() tblen=3>.value

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKSkoleIE__real_extract_0.py:26: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKSkoleIE__real_extract_0.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKSkoleIE__real_extract_0.py::test_missing_lines
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKSkoleIE__real_extract_0.py::test_invalid_input
============================== 3 failed in 0.66s ===============================
"""