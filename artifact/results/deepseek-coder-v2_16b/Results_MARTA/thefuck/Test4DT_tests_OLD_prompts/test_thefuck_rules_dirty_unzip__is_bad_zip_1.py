
import pytest
from unittest.mock import patch, MagicMock
import zipfile
from thefuck.rules.dirty_unzip import _is_bad_zip


def test_invalid_zip():
    mock_zip = MagicMock()
    mock_zip.side_effect = zipfile.BadZipFile("Not a valid zip file")
    
    with patch('zipfile.ZipFile', return_value=mock_zip):
        assert _is_bad_zip('path/to/invalid_archive.zip') is False