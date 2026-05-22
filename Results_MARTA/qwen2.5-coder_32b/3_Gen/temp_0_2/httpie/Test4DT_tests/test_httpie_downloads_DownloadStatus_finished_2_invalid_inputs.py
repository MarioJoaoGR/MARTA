
import unittest
from unittest.mock import patch, MagicMock
from httpie.downloads import DownloadStatus

class TestDownloadStatus(unittest.TestCase):
    def test_finished_with_valid_inputs(self):
        with patch('httpie.downloads.monotonic', return_value=1234567890.0):
            status = DownloadStatus(env="network_storage")
            status.time_started = 1234567890.0
            status.finished()
            self.assertIsNotNone(status.time_finished)
            self.assertEqual(status.time_finished, 1234567890.0)
