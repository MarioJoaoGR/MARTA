
import pytest
from youtube_dl.extractor.tudou import TudouAlbumIE



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tudou_TudouAlbumIE__real_extract_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        tudou_album = TudouAlbumIE()
        url = 'http://www.tudou.com/albumplay/v5qckFJvNJg.html'
>       info_dict = tudou_album._real_extract(url)

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tudou_TudouAlbumIE__real_extract_0.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/tudou.py:43: in _real_extract
    album_data = self._download_json(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:895: in _download_json
    res = self._download_json_handle(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:874: in _download_json_handle
    res = self._download_webpage_handle(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:667: in _download_webpage_handle
    urlh = self._request_webpage(url_or_request, video_id, note, errnote, fatal, data=data, headers=headers, query=query, expected_status=expected_status)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:611: in _request_webpage
    self.to_screen('%s: %s' % (video_id, note))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <youtube_dl.extractor.tudou.TudouAlbumIE object at 0x7f9642841f60>
msg = 'v5qckFJvNJg: Downloading JSON metadata'

    def to_screen(self, msg):
        """Print msg to screen, prefixing it with '[ie_name]'"""
>       self._downloader.to_screen('[%s] %s' % (self.IE_NAME, msg))
E       AttributeError: 'NoneType' object has no attribute 'to_screen'

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:921: AttributeError
____________________________ test_invalid_url_case _____________________________

    def test_invalid_url_case():
        tudou_album = TudouAlbumIE()
        url = 'http://www.tudou.com/invalid-url'
        with pytest.raises(Exception) as e:
            tudou_album._real_extract(url)
>       assert str(e.value).startswith('ERROR:'), "Expected an error message starting with 'ERROR:'"
E       AssertionError: Expected an error message starting with 'ERROR:'
E       assert False
E        +  where False = <built-in method startswith of str object at 0x7f9644d40030>('ERROR:')
E        +    where <built-in method startswith of str object at 0x7f9644d40030> = ''.startswith
E        +      where '' = str(AssertionError())
E        +        where AssertionError() = <ExceptionInfo AssertionError() tblen=3>.value

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tudou_TudouAlbumIE__real_extract_0.py:17: AssertionError
____________________________ test_missing_data_case ____________________________

    def test_missing_data_case():
        tudou_album = TudouAlbumIE()
        url = 'http://www.tudou.com/albumplay/nonexistentid'
        with pytest.raises(Exception) as e:
            tudou_album._real_extract(url)
>       assert str(e.value).startswith('ERROR:'), "Expected an error message starting with 'ERROR:'"
E       AssertionError: Expected an error message starting with 'ERROR:'
E       assert False
E        +  where False = <built-in method startswith of str object at 0x7f96426a7030>('ERROR:')
E        +    where <built-in method startswith of str object at 0x7f96426a7030> = "'NoneType' object has no attribute 'to_screen'".startswith
E        +      where "'NoneType' object has no attribute 'to_screen'" = str(AttributeError("'NoneType' object has no attribute 'to_screen'"))
E        +        where AttributeError("'NoneType' object has no attribute 'to_screen'") = <ExceptionInfo AttributeError("'NoneType' object has no attribute 'to_screen'") tblen=7>.value

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tudou_TudouAlbumIE__real_extract_0.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tudou_TudouAlbumIE__real_extract_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tudou_TudouAlbumIE__real_extract_0.py::test_invalid_url_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tudou_TudouAlbumIE__real_extract_0.py::test_missing_data_case
============================== 3 failed in 0.65s ===============================
"""