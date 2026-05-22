
import unittest
from datetime import datetime, timedelta
from httpie.downloads import DownloadStatus
from unittest.mock import patch

class TestDownloadStatus(unittest.TestCase):
    def test_time_spent_with_valid_times(self):
        with patch('httpie.downloads.datetime') as mock_datetime:
            mock_datetime.now = unittest.mock.Mock(return_value=datetime(2023, 1, 1, 12, 0, 0))
            status = DownloadStatus(env="test_env")
            status.time_started = datetime(2023, 1, 1, 12, 0, 0)
            status.time_finished = datetime(2023, 1, 1, 12, 1, 0)
            
            self.assertEqual(status.time_spent(), timedelta(minutes=1))

    def test_time_spent_with_none_times(self):
        with patch('httpie.downloads.datetime') as mock_datetime:
            mock_datetime.now = unittest.mock.Mock(return_value=datetime(2023, 1, 1, 12, 0, 0))
            status = DownloadStatus(env="test_env")
            
            self.assertIsNone(status.time_spent())

    def test_time_spent_with_only_start_time(self):
        with patch('httpie.downloads.datetime') as mock_datetime:
            mock_datetime.now = unittest.mock.Mock(return_value=datetime(2023, 1, 1, 12, 0, 0))
            status = DownloadStatus(env="test_env")
            status.time_started = datetime(2023, 1, 1, 12, 0, 0)
            
            self.assertIsNone(status.time_spent())

    def test_time_spent_with_only_finish_time(self):
        with patch('httpie.downloads.datetime') as mock_datetime:
            mock_datetime.now = unittest.mock.Mock(return_value=datetime(2023, 1, 1, 12, 0, 0))
            status = DownloadStatus(env="test_env")
            status.time_finished = datetime(2023, 1, 1, 12, 1, 0)
            
            self.assertIsNone(status.time_spent())

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_downloads_DownloadStatus_time_spent_3_test_invalid_inputs
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_DownloadStatus_time_spent_3_test_invalid_inputs.py:15:29: E1102: status.time_spent is not callable (not-callable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_DownloadStatus_time_spent_3_test_invalid_inputs.py:22:30: E1102: status.time_spent is not callable (not-callable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_DownloadStatus_time_spent_3_test_invalid_inputs.py:30:30: E1102: status.time_spent is not callable (not-callable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_DownloadStatus_time_spent_3_test_invalid_inputs.py:38:30: E1102: status.time_spent is not callable (not-callable)


"""