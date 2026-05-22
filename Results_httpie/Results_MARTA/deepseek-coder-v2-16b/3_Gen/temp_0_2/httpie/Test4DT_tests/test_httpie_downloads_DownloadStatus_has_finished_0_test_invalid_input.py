
import pytest
from datetime import datetime
from unittest.mock import patch
from httpie.downloads import DownloadStatus

def test_invalid_input():
    with patch('httpie.downloads.DownloadStatus.__init__', side_effect=TypeError):
        with pytest.raises(TypeError):
            status = DownloadStatus(env='network_storage')
