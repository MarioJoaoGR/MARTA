
import pytest
from ansible.modules.pip import Package

# Test valid case with name and version
def test_valid_case_with_version():
    pkg = Package("requests", "2.25.1")
    assert pkg.package_name == "requests"
    assert pkg._requirement.project_name == "requests"

# Test edge case without providing a version
def test_edge_case_no_version():
    pkg = Package("setuptools")
    assert pkg.package_name == "setuptools"
    assert pkg._requirement.project_name == "setuptools"

# Test invalid input that should raise ValueError
def test_invalid_input():
    with pytest.raises(ValueError):
        pkg = Package()
