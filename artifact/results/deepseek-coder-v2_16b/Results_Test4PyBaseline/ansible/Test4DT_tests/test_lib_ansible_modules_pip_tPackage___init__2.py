
import pytest
from ansible.modules.pip import Package, Requirement

# Test cases for the Package class
def test_package_init():
    # Test initialization without version string
    pkg = Package("requests")
    assert isinstance(pkg, Package)