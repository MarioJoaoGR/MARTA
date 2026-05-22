
import unittest
from unittest.mock import patch
from httpie.downloads import Downloader  # Assuming this is the correct path and module name

class TestDownloader(unittest.TestCase):
    @patch('httpie.downloads.Downloader')
    def test_interrupted(self, MockDownloader):
        # Create an instance of the MockDownloader class for testing
        mock_instance = MockDownloader.return_value
        
        # Set up the necessary attributes and methods for the mock instance
        mock_instance.finished = True  # Example state where download is finished
        mock_instance.status.total_size = 100  # Total size of the expected file
        mock_instance.status.downloaded = 50  # Amount already downloaded (interrupted)
        
        # Call the method to be tested
        self.assertTrue(mock_instance.interrupted())

if __name__ == '__main__':
    unittest.main()
