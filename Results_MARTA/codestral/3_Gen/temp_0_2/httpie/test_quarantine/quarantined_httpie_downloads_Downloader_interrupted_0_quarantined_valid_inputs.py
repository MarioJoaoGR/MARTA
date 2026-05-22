
import unittest.mock as mock
from httpie.downloads import Downloader, Environment, DownloadStatus

class TestDownloaderInterrupted(unittest.TestCase):
    @mock.patch('httpie.downloads.Environment')
    def test_interrupted_when_download_is_finished_and_total_size_equals_downloaded(self, MockEnv):
        env = MockEnv()
        downloader = Downloader(env=env, resume=True)
        downloader.status.total_size = 100
        downloader.status.downloaded = 100
        downloader.finished = True
        self.assertFalse(downloader.interrupted())

    @mock.patch('httpie.downloads.Environment')
    def test_interrupted_when_download_is_finished_and_total_size_not_equal_to_downloaded(self, MockEnv):
        env = MockEnv()
        downloader = Downloader(env=env, resume=True)
        downloader.status.total_size = 100
        downloader.status.downloaded = 50
        downloader.finished = True
        self.assertTrue(downloader.interrupted())

    @mock.patch('httpie.downloads.Environment')
    def test_interrupted_when_download_is_not_finished(self, MockEnv):
        env = MockEnv()
        downloader = Downloader(env=env, resume=True)
        downloader.status.total_size = 100
        downloader.status.downloaded = 50
        downloader.finished = False
        self.assertTrue(downloader.interrupted())

    @mock.patch('httpie.downloads.Environment')
    def test_interrupted_when_total_size_is_zero(self, MockEnv):
        env = MockEnv()
        downloader = Downloader(env=env, resume=True)
        downloader.status.total_size = 0
        downloader.status.downloaded = 0
        downloader.finished = True
        self.assertFalse(downloader.interrupted())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_downloads_Downloader_interrupted_0_test_valid_inputs
httpie/Test4DT_tests_codestral/test_httpie_downloads_Downloader_interrupted_0_test_valid_inputs.py:5:32: E0602: Undefined variable 'unittest' (undefined-variable)


"""