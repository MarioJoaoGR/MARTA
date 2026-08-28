
import pytest
from youtube_dl.extractor.tf1 import TF1IE



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tf1_TF1IE__real_extract_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

    def test_valid_case():
        extractor = TF1IE()
        url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/quotidien-premiere-partie-11-juin-2019.html'
>       info_dict = extractor._real_extract(url)

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tf1_TF1IE__real_extract_0.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/tf1.py:45: in _real_extract
    video = self._download_json(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:895: in _download_json
    res = self._download_json_handle(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:874: in _download_json_handle
    res = self._download_webpage_handle(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:667: in _download_webpage_handle
    urlh = self._request_webpage(url_or_request, video_id, note, errnote, fatal, data=data, headers=headers, query=query, expected_status=expected_status)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:611: in _request_webpage
    self.to_screen('%s: %s' % (video_id, note))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <youtube_dl.extractor.tf1.TF1IE object at 0x7fecd95727a0>
msg = 'quotidien-premiere-partie-11-juin-2019: Downloading JSON metadata'

    def to_screen(self, msg):
        """Print msg to screen, prefixing it with '[ie_name]'"""
>       self._downloader.to_screen('[%s] %s' % (self.IE_NAME, msg))
E       AttributeError: 'NoneType' object has no attribute 'to_screen'

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:921: AttributeError
______________________________ test_missing_lines ______________________________

    def test_missing_lines():
        extractor = TF1IE()
        url = 'https://www.tf1.fr/tmc/quotidien-avec-yann-barthes/videos/nonexistentvideo.html'
        with pytest.raises(Exception) as e:
            extractor._real_extract(url)
>       assert str(e.value).startswith('ERROR'), f"Expected an error, got {str(e.value)}"
E       AssertionError: Expected an error, got 'NoneType' object has no attribute 'to_screen'
E       assert False
E        +  where False = <built-in method startswith of str object at 0x7fecd93e3d50>('ERROR')
E        +    where <built-in method startswith of str object at 0x7fecd93e3d50> = "'NoneType' object has no attribute 'to_screen'".startswith
E        +      where "'NoneType' object has no attribute 'to_screen'" = str(AttributeError("'NoneType' object has no attribute 'to_screen'"))
E        +        where AttributeError("'NoneType' object has no attribute 'to_screen'") = <ExceptionInfo AttributeError("'NoneType' object has no attribute 'to_screen'") tblen=7>.value

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tf1_TF1IE__real_extract_0.py:23: AssertionError
_______________________________ test_error_case ________________________________

    def test_error_case():
        extractor = TF1IE()
        url = 'invalid-url'
        with pytest.raises(ValueError) as e:
>           extractor._real_extract(url)

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tf1_TF1IE__real_extract_0.py:29: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <youtube_dl.extractor.tf1.TF1IE object at 0x7fecd9409c00>
url = 'invalid-url'

    def _real_extract(self, url):
>       program_slug, slug = re.match(self._VALID_URL, url).groups()
E       AttributeError: 'NoneType' object has no attribute 'groups'

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/tf1.py:44: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tf1_TF1IE__real_extract_0.py::test_valid_case
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tf1_TF1IE__real_extract_0.py::test_missing_lines
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tf1_TF1IE__real_extract_0.py::test_error_case
============================== 3 failed in 0.65s ===============================
"""