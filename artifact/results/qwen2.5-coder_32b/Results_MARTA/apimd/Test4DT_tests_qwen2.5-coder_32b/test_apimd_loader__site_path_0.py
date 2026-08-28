
import pytest
from apimd.loader import _site_path


def test_non_existent_package():
    """Test that _site_path returns an empty string for a non-existent package."""
    assert _site_path('non_existent_package') == ""

def test_standard_library_module():
    """Test that _site_path returns an empty string for a standard library module."""
    assert _site_path('os') == ""
