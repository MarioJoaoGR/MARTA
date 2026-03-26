
import pytest
from unittest.mock import patch, MagicMock
from flutes.network import _download_from_google_drive

def test_invalid_input():
    with pytest.raises(Exception):
        # Providing an invalid Google Drive URL should raise an exception
        assert _download_from_google_drive("https://invalid-url.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view?usp=sharing", "myfile.txt", "/home/user")
