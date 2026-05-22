
import pytest
from httpie.downloads import DownloadStatus

def test_invalid_input():
    with pytest.raises(AttributeError):
        status = DownloadStatus("env")
        # Attempt to access a non-existent attribute to trigger an AttributeError
        getattr(status, 'display')
