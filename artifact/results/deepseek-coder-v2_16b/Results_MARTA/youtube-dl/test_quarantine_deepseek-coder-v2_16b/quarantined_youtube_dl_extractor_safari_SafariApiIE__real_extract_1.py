
import pytest
from youtube_dl.extractor import SafariApiIE



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_safari_SafariApiIE__real_extract_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________________ test_valid_url ________________________________

    def test_valid_url():
        safari_api = SafariApiIE()
        url = 'https://www.safaribooksonline.com/api/v1/book/9780133392838/chapter/part00.html'
>       info = safari_api._real_extract(url)

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_safari_SafariApiIE__real_extract_1.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/safari.py:193: in _real_extract
    part = self._download_json(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:895: in _download_json
    res = self._download_json_handle(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:874: in _download_json_handle
    res = self._download_webpage_handle(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:667: in _download_webpage_handle
    urlh = self._request_webpage(url_or_request, video_id, note, errnote, fatal, data=data, headers=headers, query=query, expected_status=expected_status)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:611: in _request_webpage
    self.to_screen('%s: %s' % (video_id, note))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <youtube_dl.extractor.safari.SafariApiIE object at 0x7fd82ab30520>
msg = '9780133392838/part00: Downloading part JSON'

    def to_screen(self, msg):
        """Print msg to screen, prefixing it with '[ie_name]'"""
>       self._downloader.to_screen('[%s] %s' % (self.IE_NAME, msg))
E       AttributeError: 'NoneType' object has no attribute 'to_screen'

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:921: AttributeError
_______________________________ test_invalid_url _______________________________

    def test_invalid_url():
        safari_api = SafariApiIE()
        invalid_url = 'https://www.example.com/invalid-path'
        with pytest.raises(Exception) as e:
            safari_api._real_extract(invalid_url)
>       assert "Unable to extract URL" in str(e.value), "Expected an error message about unable to extract URL"
E       AssertionError: Expected an error message about unable to extract URL
E       assert 'Unable to extract URL' in "'NoneType' object has no attribute 'group'"
E        +  where "'NoneType' object has no attribute 'group'" = str(AttributeError("'NoneType' object has no attribute 'group'"))
E        +    where AttributeError("'NoneType' object has no attribute 'group'") = <ExceptionInfo AttributeError("'NoneType' object has no attribute 'group'") tblen=2>.value

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_safari_SafariApiIE__real_extract_1.py:17: AssertionError
______________________________ test_missing_lines ______________________________

    def test_missing_lines():
        safari_api = SafariApiIE()
        url = 'https://www.safaribooksonline.com/api/v1/book/9780133392838/chapter/part00.html'
        with pytest.raises(Exception) as e:
            safari_api._real_extract(url)
>       assert "Unable to extract URL" in str(e.value), "Expected an error message about unable to extract URL"
E       AssertionError: Expected an error message about unable to extract URL
E       assert 'Unable to extract URL' in "'NoneType' object has no attribute 'to_screen'"
E        +  where "'NoneType' object has no attribute 'to_screen'" = str(AttributeError("'NoneType' object has no attribute 'to_screen'"))
E        +    where AttributeError("'NoneType' object has no attribute 'to_screen'") = <ExceptionInfo AttributeError("'NoneType' object has no attribute 'to_screen'") tblen=7>.value

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_safari_SafariApiIE__real_extract_1.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_safari_SafariApiIE__real_extract_1.py::test_valid_url
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_safari_SafariApiIE__real_extract_1.py::test_invalid_url
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_safari_SafariApiIE__real_extract_1.py::test_missing_lines
============================== 3 failed in 0.65s ===============================
"""