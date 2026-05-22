
import unittest
from unittest.mock import patch
from httpie.ssl_ import _is_key_file_encrypted

class TestIsKeyFileEncrypted(unittest.TestCase):
    @patch('httpie.ssl_.open', create=True)
    def test_none_input(self, mock_open):
        # Mock the file object to return an empty string for read operations
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.side_effect = [""]  # First call returns "", subsequent calls also return ""

        result = _is_key_file_encrypted("dummy_path")
        self.assertFalse(result)
