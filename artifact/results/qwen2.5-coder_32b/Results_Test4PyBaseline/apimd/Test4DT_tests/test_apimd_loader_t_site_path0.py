
import pytest
from apimd.loader import _site_path

def test_site_path_existing_package():
    # Assuming 'numpy' is installed, this should return a non-empty string path.
    path = _site_path('numpy')
    assert isinstance(path, str)
    assert len(path) > 0

def test_site_path_another_existing_package():
    # Assuming 'pandas' is installed, this should return a non-empty string path.
    path = _site_path('pandas')
    assert isinstance(path, str)