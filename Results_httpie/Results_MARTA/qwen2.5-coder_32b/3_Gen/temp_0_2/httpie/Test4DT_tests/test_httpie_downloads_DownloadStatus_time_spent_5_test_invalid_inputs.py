
import pytest
from datetime import datetime, timedelta
from unittest.mock import patch
from httpie.downloads import DownloadStatus

def test_invalid_inputs():
    with patch('datetime.datetime') as mock_datetime:
        status = DownloadStatus(env='network_storage')
        status.downloaded = 1024
        status.total_size = 102400
        status.resumed_from = 0
        
        # Mock datetime to raise TypeError when time_started is None
        mock_datetime.now.side_effect = TypeError("Mocked TypeError")
        
        with pytest.raises(TypeError):
            status.time_started = mock_datetime.now()
