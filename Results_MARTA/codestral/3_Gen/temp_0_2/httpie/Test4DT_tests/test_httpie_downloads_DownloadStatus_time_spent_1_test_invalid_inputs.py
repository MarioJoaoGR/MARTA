
import pytest
from unittest.mock import patch
from datetime import datetime, timedelta
from httpie.downloads import DownloadStatus

def test_invalid_inputs():
    with patch('builtins.isinstance', side_effect=TypeError):
        status = DownloadStatus(env="network_storage")
        status.downloaded = "not an int"
        status.total_size = "also not an int"
        status.resumed_from = "definitely not an int"
        status.time_started = datetime.now()
        status.time_finished = datetime.now()
    
    with pytest.raises(TypeError):
        status.time_spent()
