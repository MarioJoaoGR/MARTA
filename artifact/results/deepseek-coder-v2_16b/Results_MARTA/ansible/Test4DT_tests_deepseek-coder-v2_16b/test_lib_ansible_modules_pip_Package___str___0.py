
import pytest
from ansible.modules.pip import Package
import re

# Test valid case with version specifier
def test_valid_case_with_version():
    pkg = Package('requests', '2.25.1')
    assert pkg.package_name == 'requests'
    assert pkg._requirement.project_name == 'requests'
    assert str(pkg) == 'requests==2.25.1'

# Test edge case without version specifier
def test_edge_case_no_version():
    pkg = Package('setuptools')
    assert pkg.package_name == 'setuptools'
    assert pkg._requirement.project_name == 'setuptools'
    assert str(pkg) == 'setuptools'

# Test raising ValueError with invalid input
def test_invalid_input():
    try:
        pkg = Package('invalid-package', 'invalid-version')
    except ValueError as e:
        assert "Invalid package name or version" in str(e)
