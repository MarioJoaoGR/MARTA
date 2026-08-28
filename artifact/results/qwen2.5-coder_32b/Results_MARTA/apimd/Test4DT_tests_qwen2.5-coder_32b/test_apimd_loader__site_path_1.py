
import pytest
from apimd.loader import _site_path






def test_valid_package_installed():
    # Test with a valid installed package name
    valid_input = 'os'  # os is part of the standard library and does not have a site-packages entry
    path = _site_path(valid_input)
    assert path == ""

def test_non_existent_package():
    # Test with a non-existent package name
    invalid_input = 'non_existent_package'
    path = _site_path(invalid_input)  # This should handle non-existent package gracefully
    assert path == ""