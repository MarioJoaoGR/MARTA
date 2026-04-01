
import pytest
from unittest.mock import patch, MagicMock
from flutes.network import _download_from_google_drive

@pytest.mark.parametrize("url", ["invalid_url"])
def test_invalid_input(url):
    with pytest.raises(Exception):
        _download_from_google_drive(url, "filename", "/path")
