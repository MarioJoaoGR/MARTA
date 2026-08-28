
import pytest
from unittest.mock import patch
from youtube_dl.extractor.linuxacademy import LinuxAcademyIE



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__login_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
____________________________ test_valid_credentials ____________________________

    def test_valid_credentials():
        with patch('youtube_dl.extractor.linuxacademy.LinuxAcademyIE._get_login_info', return_value=('valid_username', 'valid_password')):
            ie = LinuxAcademyIE()
            with pytest.raises(NotImplementedError):
>               ie._login()

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__login_0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/linuxacademy.py:82: in _login
    webpage, urlh = self._download_webpage_handle(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:667: in _download_webpage_handle
    urlh = self._request_webpage(url_or_request, video_id, note, errnote, fatal, data=data, headers=headers, query=query, expected_status=expected_status)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:609: in _request_webpage
    self.to_screen('%s' % (note,))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <youtube_dl.extractor.linuxacademy.LinuxAcademyIE object at 0x7f05ea5a56f0>
msg = 'Downloading authorize page'

    def to_screen(self, msg):
        """Print msg to screen, prefixing it with '[ie_name]'"""
>       self._downloader.to_screen('[%s] %s' % (self.IE_NAME, msg))
E       AttributeError: 'NoneType' object has no attribute 'to_screen'

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:921: AttributeError
___________________________ test_missing_credentials ___________________________

    def test_missing_credentials():
        with patch('youtube_dl.extractor.linuxacademy.LinuxAcademyIE._get_login_info', return_value=(None, None)):
            ie = LinuxAcademyIE()
>           with pytest.raises(NotImplementedError):
E           Failed: DID NOT RAISE <class 'NotImplementedError'>

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__login_0.py:15: Failed
___________________________ test_invalid_credentials ___________________________

    def test_invalid_credentials():
        with patch('youtube_dl.extractor.linuxacademy.LinuxAcademyIE._get_login_info', return_value=('invalid_username', 'invalid_password')):
            ie = LinuxAcademyIE()
            with pytest.raises(NotImplementedError):
>               ie._login()

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__login_0.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/linuxacademy.py:82: in _login
    webpage, urlh = self._download_webpage_handle(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:667: in _download_webpage_handle
    urlh = self._request_webpage(url_or_request, video_id, note, errnote, fatal, data=data, headers=headers, query=query, expected_status=expected_status)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:609: in _request_webpage
    self.to_screen('%s' % (note,))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <youtube_dl.extractor.linuxacademy.LinuxAcademyIE object at 0x7f05ea412ad0>
msg = 'Downloading authorize page'

    def to_screen(self, msg):
        """Print msg to screen, prefixing it with '[ie_name]'"""
>       self._downloader.to_screen('[%s] %s' % (self.IE_NAME, msg))
E       AttributeError: 'NoneType' object has no attribute 'to_screen'

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:921: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__login_0.py::test_valid_credentials
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__login_0.py::test_missing_credentials
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__login_0.py::test_invalid_credentials
============================== 3 failed in 0.76s ===============================
"""