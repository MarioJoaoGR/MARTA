
import pytest
from ansible.modules.pip import Package, Requirement

# Test Scenario 1: Creating a Package instance with a version specifier
def test_package_creation_with_version():
    pkg = Package("requests", "2.25.1")
    assert pkg.package_name == "requests"
    assert isinstance(pkg._requirement, Requirement)

# Test Scenario 2: Creating a Package instance without specifying a version
def test_package_creation_without_version():
    pkg = Package("setuptools")
    assert pkg.package_name == "setuptools"
    assert isinstance(pkg._requirement, Requirement)

# Test Scenario 3: Checking if the package has a version specifier

# Test Scenario 4: Canonicalizing package names