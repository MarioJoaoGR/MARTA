
import pytest
from unittest.mock import patch
import os
from semantic_release.pypi import upload_to_pypi
from semantic_release.errors import ImproperConfigurationError

def test_upload_to_pypi_default():
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi()

def test_upload_to_pypi_custom_path():
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi(path="custom_dist")

def test_upload_to_pypi_skip_existing():
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi(skip_existing=True)

def test_upload_to_pypi_glob_patterns():
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi(glob_patterns=["*.whl", "*.tar.gz"])

def test_upload_to_pypi_all_parameters():
    with pytest.raises(ImproperConfigurationError):
        upload_to_pypi(path="custom_dist", skip_existing=True, glob_patterns=["*.whl"])
