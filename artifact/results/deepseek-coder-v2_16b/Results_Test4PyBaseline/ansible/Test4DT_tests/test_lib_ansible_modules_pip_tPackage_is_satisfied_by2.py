
import pytest
from ansible.modules.pip import Package
import re

# Test initialization with different versions and names
def test_package_initialization():
    pkg = Package("requests")
    assert pkg.package_name == "requests" or pkg.package_name == "setuptools", f"Expected package name to be 'requests' or 'setuptools', but got {pkg.package_name}"
    
    pkg_with_version = Package("pytest", ">=5.0.1")
    assert pkg_with_version.package_name == "pytest", f"Expected package name to be 'pytest', but got {pkg_with_version.package_name}"

# Test is_satisfied_by method with valid and invalid versions
def test_is_satisfied_by():
    pkg_with_version = Package("pytest", ">=5.0.1")
    assert pkg_with_version.is_satisfied_by("5.4.3"), f"Expected is_satisfied_by('5.4.3') to be True, but got False"
    
    invalid_pkg = Package("nonexistentpackage", "1.0.0")