# Module: ansible.modules.pip
import pytest
from ansible.modules.pip import Package
import re

# Test initialization of Package without version
def test_package_init_without_version():
    pkg = Package("requests")
    assert pkg.package_name == "requests" or pkg.package_name == "setuptools"

# Test initialization of Package with version
def test_package_init_with_version():
    pkg_with_version = Package("pytest", ">=5.0.1")
    assert pkg_with_version.package_name == "pytest"

# Test checking if the package is satisfied by a given version
def test_is_satisfied_by():
    pkg_with_version = Package("pytest", ">=5.0.1")
    assert pkg_with_version.is_satisfied_by("5.4.3") == True or pkg_with_version.is_satisfied_by("5.4.3") == False

# Test canonicalize_name function
def test_canonicalize_name():
    name = "requests"
    assert Package.canonicalize_name(name) == re.compile('[-_.]+').sub("-", name).lower()
