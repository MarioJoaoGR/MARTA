
import pytest
from unittest.mock import patch
from semantic_release.pypi import upload_to_pypi
from semantic_release.errors import ImproperConfigurationError
import os


def test_upload_to_pypi_missing_credentials():
    with patch('os.environ', {'PYPI_TOKEN': 'fake_token'}):
        with pytest.raises(ImproperConfigurationError):
            upload_to_pypi(path='dist', skip_existing=True, glob_patterns=['*.whl'])

def test_upload_to_pypi_invalid_token():
    with patch('os.environ', {'PYPI_TOKEN': 'not_a_valid_token'}):
        with pytest.raises(ImproperConfigurationError):
            upload_to_pypi(path='dist', skip_existing=True, glob_patterns=['*.whl'])