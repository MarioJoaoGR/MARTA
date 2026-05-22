
import unittest
from unittest.mock import patch
from httpie.downloads import Downloader, Environment
from io import BytesIO

class TestDownloader(unittest.TestCase):
    
    @patch('httpie.downloads.Environment')
    def setUp(self, MockEnvClass):
        # Create a mock environment for the test
        self.env = MockEnvClass.return_value
        self.output_file = BytesIO()
        self.downloader = Downloader(env=self.env, output_file=self.output_file, resume=False)
    
    def test_chunk_downloaded_invalid_input(self):
        # Test that chunk_downloaded raises a TypeError when given an invalid input type (e.g., None or int)
        with self.assertRaises(TypeError):
            self.downloader.chunk_downloaded(chunk=None)  # Passing None should raise a TypeError
            self.downloader.chunk_downloaded(chunk=12345)  # Passing an integer should raise a TypeError

if __name__ == '__main__':
    unittest.main()
