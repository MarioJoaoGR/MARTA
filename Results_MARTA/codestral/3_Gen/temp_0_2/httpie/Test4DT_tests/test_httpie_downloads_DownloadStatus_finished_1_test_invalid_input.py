
import unittest
from httpie.downloads import DownloadStatus
from unittest.mock import patch, MagicMock

class TestDownloadStatus(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaises(AssertionError):
            status = DownloadStatus("invalid_env")
            status.finished()
