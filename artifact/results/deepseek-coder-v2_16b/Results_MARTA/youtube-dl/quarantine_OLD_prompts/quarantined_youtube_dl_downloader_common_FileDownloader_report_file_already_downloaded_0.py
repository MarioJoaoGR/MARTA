
import pytest
from unittest.mock import MagicMock, patch
from youtube_dl.downloader.common import FileDownloader

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_report_file_already_downloaded_0.py F [100%]

=================================== FAILURES ===================================
_____________________ test_report_file_already_downloaded ______________________

    def test_report_file_already_downloaded():
        ydl = MagicMock()
        params = {}
        downloader = FileDownloader(ydl, params)
        with patch('builtins.print') as mock_print:
            downloader.report_file_already_downloaded("testfile")
>           mock_print.assert_called_with('[download] testfile has already been downloaded')

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_report_file_already_downloaded_0.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <MagicMock name='print' id='140688322117536'>
args = ('[download] testfile has already been downloaded',), kwargs = {}
expected = "print('[download] testfile has already been downloaded')"
actual = 'not called.'
error_message = "expected call not found.\nExpected: print('[download] testfile has already been downloaded')\nActual: not called."

    def assert_called_with(self, /, *args, **kwargs):
        """assert that the last call was made with the specified arguments.
    
        Raises an AssertionError if the args and keyword args passed in are
        different to the last call to the mock."""
        if self.call_args is None:
            expected = self._format_mock_call_signature(args, kwargs)
            actual = 'not called.'
            error_message = ('expected call not found.\nExpected: %s\nActual: %s'
                    % (expected, actual))
>           raise AssertionError(error_message)
E           AssertionError: expected call not found.
E           Expected: print('[download] testfile has already been downloaded')
E           Actual: not called.

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:920: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_downloader_common_FileDownloader_report_file_already_downloaded_0.py::test_report_file_already_downloaded
============================== 1 failed in 1.15s ===============================
"""