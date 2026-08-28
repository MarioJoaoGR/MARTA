
import pytest
from your_package_manager import PkgMgr  # Replace with actual import if necessary

@pytest.fixture
def pkg_mgr():
    return PkgMgr()

# Test for valid input
def test_valid_input(pkg_mgr):
    details = pkg_mgr.get_package_details("numpy")
    assert isinstance(details, dict), "Expected a dictionary"
    assert "name" in details, "Expected 'name' key in the dictionary"
    assert "version" in details, "Expected 'version' key in the dictionary"
    assert details["name"] == "numpy", f"Expected name to be 'numpy', but got {details['name']}"
    assert isinstance(details["version"], str), "Expected version to be a string"

# Test for None input
def test_none_input(pkg_mgr):
    details = pkg_mgr.get_package_details(None)
    assert isinstance(details, dict), "Expected a dictionary"
    assert "name" not in details, "Did not expect 'name' key when input is None"
    assert "version" not in details, "Did not expect 'version' key when input is None"

# Test for invalid input (non-string)
def test_invalid_input(pkg_mgr):
    with pytest.raises(TypeError):
        details = pkg_mgr.get_package_details(123)
