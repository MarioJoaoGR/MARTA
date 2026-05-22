
import pytest
from unittest.mock import patch
from httpie.downloads import Downloader, Environment, DownloadStatus
from io import BytesIO

def test_chunk_downloaded():
    # Mock the environment
    env = Environment(config={"network": "example.com"})
    
    # Create a mock output file
    output_file = BytesIO()
    
    # Initialize the Downloader with the mocked environment and output file
    downloader = Downloader(env=env, output_file=output_file, resume=True)
    
    # Mock the chunk data to simulate downloading a chunk of data
    chunk_data = b'some_chunk_data'
    
    # Use patch to mock the method call and check if it updates the status correctly
    with patch.object(DownloadStatus, 'chunk_downloaded') as mock_chunk_downloaded:
        downloader.chunk_downloaded(chunk=chunk_data)
        
        # Assert that the chunk_downloaded method of DownloadStatus was called with the correct argument
        mock_chunk_downloaded.assert_called_with(len(chunk_data))
