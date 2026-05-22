
import unittest
from datetime import datetime, timedelta
from httpie.downloads import DownloadStatus
from unittest.mock import patch

class TestDownloadStatus(unittest.TestCase):
    def setUp(self):
        self.env = "network_storage"
        self.download_status = DownloadStatus(self.env)

    @patch('httpie.downloads.datetime')
    def test_time_spent_fully_elapsed(self, mock_datetime):
        # Set the start time to a known point in the past
        mock_datetime.now.return_value = datetime.now() - timedelta(seconds=10)
        self.download_status.time_started = mock_datetime.now.return_value
        
        # Set the finish time to a known point in the future (fully elapsed)
        mock_datetime.now.return_value += timedelta(seconds=5)
        self.download_status.time_finished = mock_datetime.now.return_value
        
        self.assertEqual(self.download_status.time_spent(), timedelta(seconds=5))

    @patch('httpie.downloads.datetime')
    def test_time_spent_not_fully_elapsed(self, mock_datetime):
        # Set the start time to a known point in the past
        mock_datetime.now.return_value = datetime.now() - timedelta(seconds=10)
        self.download_status.time_started = mock_datetime.now.return_value
        
        # The finish time is not set yet (still ongoing)
        self.assertIsNone(self.download_status.time_finished)
        self.assertIsNone(self.download_status.time_spent())

    @patch('httpie.downloads.datetime')
    def test_time_spent_no_start_or_finish(self, mock_datetime):
        # Neither start nor finish time is set
        self.assertIsNone(self.download_status.time_started)
        self.assertIsNone(self.download_status.time_finished)
        self.assertIsNone(self.download_status.time_spent())

if __name__ == '__main__':
    unittest.main()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_downloads_DownloadStatus_time_spent_1_test_edge_cases
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_DownloadStatus_time_spent_1_test_edge_cases.py:22:25: E1102: self.download_status.time_spent is not callable (not-callable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_DownloadStatus_time_spent_1_test_edge_cases.py:32:26: E1102: self.download_status.time_spent is not callable (not-callable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_DownloadStatus_time_spent_1_test_edge_cases.py:39:26: E1102: self.download_status.time_spent is not callable (not-callable)


"""