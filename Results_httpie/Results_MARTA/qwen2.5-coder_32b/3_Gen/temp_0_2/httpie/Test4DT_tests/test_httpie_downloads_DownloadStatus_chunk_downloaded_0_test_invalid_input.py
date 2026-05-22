
import pytest
from unittest.mock import patch
from httpie.downloads import DownloadStatus

def test_invalid_input():
    with patch('httpie.downloads.DownloadStatus.__init__', side_effect=ValueError):
        with pytest.raises(ValueError):
            download_status = DownloadStatus(env='invalid_environment')
