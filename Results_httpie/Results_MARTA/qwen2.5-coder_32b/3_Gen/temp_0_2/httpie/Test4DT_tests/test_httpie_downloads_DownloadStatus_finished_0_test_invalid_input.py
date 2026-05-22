
import pytest
from unittest.mock import patch, MagicMock
from httpie.downloads import DownloadStatus

def test_invalid_input():
    with pytest.raises(AssertionError):
        status = DownloadStatus(env="network_storage")
        status.finished()
