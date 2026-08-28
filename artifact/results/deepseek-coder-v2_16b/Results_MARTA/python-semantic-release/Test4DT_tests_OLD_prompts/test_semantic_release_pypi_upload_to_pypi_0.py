
import pytest
from unittest.mock import patch
from semantic_release.pypi import upload_to_pypi
from semantic_release.errors import ImproperConfigurationError
import os

def test_valid_inputs():
    with patch('os.environ', {'PYPI_TOKEN': 'valid-token'}):
        with pytest.raises(ImproperConfigurationError):
            upload_to_pypi()

def test_edge_cases():
    with patch('os.environ', {'PYPI_TOKEN': None}):
        with pytest.raises(ImproperConfigurationError):
            upload_to_pypi()

def test_invalid_inputs():
    with patch('os.environ', {'PYPI_TOKEN': 'improper-token'}):
        with pytest.raises(ImproperConfigurationError):
            upload_to_pypi()
