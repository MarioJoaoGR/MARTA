
import unittest
from unittest.mock import patch, MagicMock
from httpie.downloads import Downloader, Environment, DownloadStatus

class TestDownloaderInterrupted(unittest.TestCase):
    
    @patch('httpie.downloads.Environment')
    def test_interrupted_when_download_is_finished_and_total_size_equals_downloaded(self, MockEnv):
        env = MockEnv()
        downloader = Downloader(env=env, resume=True)
        downloader.status.downloaded = 100
        downloader.status.total_size = 100
        self.assertFalse(downloader.interrupted())

    @patch('httpie.downloads.Environment')
    def test_interrupted_when_download_is_finished_and_total_size_not_equals_downloaded(self, MockEnv):
        env = MockEnv()
        downloader = Downloader(env=env, resume=True)
        downloader.status.downloaded = 90
        downloader.status.total_size = 100
        self.assertTrue(downloader.interrupted())

    @patch('httpie.downloads.Environment')
    def test_interrupted_when_download_is_not_finished(self, MockEnv):
        env = MockEnv()
        downloader = Downloader(env=env, resume=True)
        downloader.status.downloaded = 0
        downloader.status.total_size = 100
        self.assertFalse(downloader.interrupted())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_Downloader_interrupted_0_test_edge_case.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_ TestDownloaderInterrupted.test_interrupted_when_download_is_finished_and_total_size_equals_downloaded _

self = <test_httpie_downloads_Downloader_interrupted_0_test_edge_case.TestDownloaderInterrupted testMethod=test_interrupted_when_download_is_finished_and_total_size_equals_downloaded>
MockEnv = <MagicMock name='Environment' id='139885685217936'>

    @patch('httpie.downloads.Environment')
    def test_interrupted_when_download_is_finished_and_total_size_equals_downloaded(self, MockEnv):
        env = MockEnv()
        downloader = Downloader(env=env, resume=True)
        downloader.status.downloaded = 100
        downloader.status.total_size = 100
>       self.assertFalse(downloader.interrupted())
E       TypeError: 'bool' object is not callable

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_Downloader_interrupted_0_test_edge_case.py:14: TypeError
_ TestDownloaderInterrupted.test_interrupted_when_download_is_finished_and_total_size_not_equals_downloaded _

self = <test_httpie_downloads_Downloader_interrupted_0_test_edge_case.TestDownloaderInterrupted testMethod=test_interrupted_when_download_is_finished_and_total_size_not_equals_downloaded>
MockEnv = <MagicMock name='Environment' id='139885677566544'>

    @patch('httpie.downloads.Environment')
    def test_interrupted_when_download_is_finished_and_total_size_not_equals_downloaded(self, MockEnv):
        env = MockEnv()
        downloader = Downloader(env=env, resume=True)
        downloader.status.downloaded = 90
        downloader.status.total_size = 100
>       self.assertTrue(downloader.interrupted())
E       TypeError: 'bool' object is not callable

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_Downloader_interrupted_0_test_edge_case.py:22: TypeError
___ TestDownloaderInterrupted.test_interrupted_when_download_is_not_finished ___

self = <test_httpie_downloads_Downloader_interrupted_0_test_edge_case.TestDownloaderInterrupted testMethod=test_interrupted_when_download_is_not_finished>
MockEnv = <MagicMock name='Environment' id='139885677547280'>

    @patch('httpie.downloads.Environment')
    def test_interrupted_when_download_is_not_finished(self, MockEnv):
        env = MockEnv()
        downloader = Downloader(env=env, resume=True)
        downloader.status.downloaded = 0
        downloader.status.total_size = 100
>       self.assertFalse(downloader.interrupted())
E       TypeError: 'bool' object is not callable

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_Downloader_interrupted_0_test_edge_case.py:30: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_Downloader_interrupted_0_test_edge_case.py::TestDownloaderInterrupted::test_interrupted_when_download_is_finished_and_total_size_equals_downloaded
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_Downloader_interrupted_0_test_edge_case.py::TestDownloaderInterrupted::test_interrupted_when_download_is_finished_and_total_size_not_equals_downloaded
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_Downloader_interrupted_0_test_edge_case.py::TestDownloaderInterrupted::test_interrupted_when_download_is_not_finished
============================== 3 failed in 0.18s ===============================
"""