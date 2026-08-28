
import pytest
from apimd.loader import _site_path
from importlib.util import find_spec
from os.path import dirname

def test_valid_installed_package():
    # Assuming 'numpy' is installed in the environment
    package_name = 'numpy'
    path = _site_path(package_name)
    assert path != "", f"Expected a non-empty path for '{package_name}', got: {path}"

def test_standard_library_module():
    # Standard library modules are not typically in site-packages
    package_name = 'os'
    path = _site_path(package_name)
    assert path == "", f"Expected an empty path for standard library module '{package_name}', got: {path}"

def test_non_existent_package():
    # Test with a non-existent package
    package_name = 'non_existent_package'
    path = _site_path(package_name)
    assert path == "", f"Expected an empty path for non-existent package '{package_name}', got: {path}"
