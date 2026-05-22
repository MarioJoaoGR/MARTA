
import pytest
from unittest.mock import patch
from httpie.downloads import DownloadStatus
from datetime import datetime

def test_invalid_input():
    with patch('httpie.downloads.DownloadStatus.__init__', side_effect=TypeError):
        with pytest.raises(TypeError):
            DownloadStatus(env=123)
