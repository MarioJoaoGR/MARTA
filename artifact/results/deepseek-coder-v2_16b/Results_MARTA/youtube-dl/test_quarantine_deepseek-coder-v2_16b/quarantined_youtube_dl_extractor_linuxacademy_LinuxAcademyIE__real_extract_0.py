
import pytest
from youtube_dl.extractor.linuxacademy import LinuxAcademyIE

# Test for valid course lesson extraction

# Test for valid module view extraction
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__real_extract_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________________________ test_valid_course_lesson ___________________________

    def test_valid_course_lesson():
        extractor = LinuxAcademyIE()
        url = 'https://linuxacademy.com/cp/courses/lesson/course/7971/lesson/2'
>       info_dict = extractor._real_extract(url)

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__real_extract_0.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/linuxacademy.py:159: in _real_extract
    webpage = self._download_webpage(url, item_id)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:798: in _download_webpage
    res = self._download_webpage_handle(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:667: in _download_webpage_handle
    urlh = self._request_webpage(url_or_request, video_id, note, errnote, fatal, data=data, headers=headers, query=query, expected_status=expected_status)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:606: in _request_webpage
    self.report_download_webpage(video_id)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:929: in report_download_webpage
    self.to_screen('%s: Downloading webpage' % video_id)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <youtube_dl.extractor.linuxacademy.LinuxAcademyIE object at 0x7f759b57b1f0>
msg = '7971-2: Downloading webpage'

    def to_screen(self, msg):
        """Print msg to screen, prefixing it with '[ie_name]'"""
>       self._downloader.to_screen('[%s] %s' % (self.IE_NAME, msg))
E       AttributeError: 'NoneType' object has no attribute 'to_screen'

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:921: AttributeError
____________________________ test_valid_module_view ____________________________

    def test_valid_module_view():
        extractor = LinuxAcademyIE()
        url = 'https://linuxacademy.com/cp/modules/view/id/154'
>       info_dict = extractor._real_extract(url)

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__real_extract_0.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/linuxacademy.py:159: in _real_extract
    webpage = self._download_webpage(url, item_id)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:798: in _download_webpage
    res = self._download_webpage_handle(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:667: in _download_webpage_handle
    urlh = self._request_webpage(url_or_request, video_id, note, errnote, fatal, data=data, headers=headers, query=query, expected_status=expected_status)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:606: in _request_webpage
    self.report_download_webpage(video_id)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:929: in report_download_webpage
    self.to_screen('%s: Downloading webpage' % video_id)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <youtube_dl.extractor.linuxacademy.LinuxAcademyIE object at 0x7f759b438fa0>
msg = '154: Downloading webpage'

    def to_screen(self, msg):
        """Print msg to screen, prefixing it with '[ie_name]'"""
>       self._downloader.to_screen('[%s] %s' % (self.IE_NAME, msg))
E       AttributeError: 'NoneType' object has no attribute 'to_screen'

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:921: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__real_extract_0.py::test_valid_course_lesson
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_linuxacademy_LinuxAcademyIE__real_extract_0.py::test_valid_module_view
============================== 2 failed in 0.74s ===============================
"""