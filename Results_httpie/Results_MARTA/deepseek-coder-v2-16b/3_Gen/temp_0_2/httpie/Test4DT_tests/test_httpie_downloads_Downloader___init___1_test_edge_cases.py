
import pytest
from unittest.mock import patch
from httpie.downloads import Downloader, Environment, DownloadStatus
from io import BytesIO

def test_downloader_init():
    env = Environment(config={"network": "example.com"})
    output_file = BytesIO()
    
    with patch('httpie.downloads.DownloadStatus', autospec=True) as mock_status:
        downloader = Downloader(env=env, output_file=output_file, resume=False)
        
        assert downloader.finished is False
        assert isinstance(downloader.status, DownloadStatus)
        assert downloader._output_file == output_file
        assert downloader._resume is False
        assert downloader._resumed_from == 0
        mock_status.assert_called_once_with(env=env)
