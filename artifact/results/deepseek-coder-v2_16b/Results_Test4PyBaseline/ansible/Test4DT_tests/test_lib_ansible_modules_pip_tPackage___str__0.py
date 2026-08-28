
import pytest
from ansible.modules.pip import Package
import re

# Test creating a Package instance for a package without a specific version
def test_create_package_without_version():
    pkg = Package("requests")
    assert pkg.package_name == "requests"