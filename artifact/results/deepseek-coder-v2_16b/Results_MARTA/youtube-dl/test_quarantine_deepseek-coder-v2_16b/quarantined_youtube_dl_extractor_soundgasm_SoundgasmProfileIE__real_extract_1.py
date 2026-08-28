
import pytest
from youtube_dl.extractor.soundgasm import SoundgasmProfileIE


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_soundgasm_SoundgasmProfileIE__real_extract_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        extractor = SoundgasmProfileIE()
        url = 'http://soundgasm.net/u/ytdl'
>       info_dict = extractor._real_extract(url)

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_soundgasm_SoundgasmProfileIE__real_extract_1.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/soundgasm.py:71: in _real_extract
    webpage = self._download_webpage(url, profile_id)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:798: in _download_webpage
    res = self._download_webpage_handle(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:667: in _download_webpage_handle
    urlh = self._request_webpage(url_or_request, video_id, note, errnote, fatal, data=data, headers=headers, query=query, expected_status=expected_status)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:606: in _request_webpage
    self.report_download_webpage(video_id)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:929: in report_download_webpage
    self.to_screen('%s: Downloading webpage' % video_id)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <youtube_dl.extractor.soundgasm.SoundgasmProfileIE object at 0x7eff98139960>
msg = 'ytdl: Downloading webpage'

    def to_screen(self, msg):
        """Print msg to screen, prefixing it with '[ie_name]'"""
>       self._downloader.to_screen('[%s] %s' % (self.IE_NAME, msg))
E       AttributeError: 'NoneType' object has no attribute 'to_screen'

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:921: AttributeError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        extractor = SoundgasmProfileIE()
        url = 'http://invalidurl.com'
        with pytest.raises(Exception) as e:
            info_dict = extractor._real_extract(url)
>       assert str(e.value).startswith("ERROR: Unable to extract profile ID from URL"), f"Expected an error about invalid URL but got {str(e.value)}"
E       AssertionError: Expected an error about invalid URL but got 
E       assert False
E        +  where False = <built-in method startswith of str object at 0x7eff9a618030>('ERROR: Unable to extract profile ID from URL')
E        +    where <built-in method startswith of str object at 0x7eff9a618030> = ''.startswith
E        +      where '' = str(AssertionError())
E        +        where AssertionError() = <ExceptionInfo AssertionError() tblen=3>.value

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_soundgasm_SoundgasmProfileIE__real_extract_1.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_soundgasm_SoundgasmProfileIE__real_extract_1.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_soundgasm_SoundgasmProfileIE__real_extract_1.py::test_invalid_input
============================== 2 failed in 0.66s ===============================
"""