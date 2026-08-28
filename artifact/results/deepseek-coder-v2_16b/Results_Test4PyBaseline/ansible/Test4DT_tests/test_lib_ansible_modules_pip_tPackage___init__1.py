
import pytest
from ansible.modules.pip import Package, Requirement

# Test cases for the Package class
def test_package_creation():
    pkg = Package("requests")
    assert isinstance(pkg, Package)
    assert pkg.package_name == "requests"