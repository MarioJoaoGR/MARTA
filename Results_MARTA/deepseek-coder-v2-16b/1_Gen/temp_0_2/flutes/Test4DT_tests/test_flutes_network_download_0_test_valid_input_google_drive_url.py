
import pytest
from unittest.mock import patch, MagicMock
import os
import tempfile
import tarfile
import zipfile
from flutes.network import download

@pytest.mark.parametrize("url", ["https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view"])
def test_valid_input_google_drive_url(url):
    with patch('flutes.network._download_from_google_drive', return_value='mocked_path'):
        with patch('os.makedirs') as makedirs_mock:
            with patch('tempfile.gettempdir', return_value='/tmp'):
                with patch('tarfile.is_tarfile', return_value=False):
                    with patch('zipfile.is_zipfile', return_value=False):
                        result = download(url, save_dir='.', filename=None, extract=False, progress=False)
                        assert result == 'mocked_path'
                        makedirs_mock.assert_called_once_with('.', exist_ok=True)
