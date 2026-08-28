
import pytest
from your_module_name import Package  # Replace 'your_module_name' with the actual module name where Package is defined

# Test for valid case with version specifier
def test_valid_case_with_version():
    pkg = Package('requests', '2.25.1')
    assert pkg.package_name == 'requests'
    assert str(pkg) == "requests==2.25.1"

# Test for edge case without version specifier
def test_edge_case_no_version():
    pkg = Package('setuptools')
    assert pkg.package_name == 'setuptools'
    assert str(pkg) == "setuptools"

# Test for invalid input raising ValueError
def test_invalid_input():
    with pytest.raises(ValueError):
        pkg = Package('invalid_package', 'invalid_version')
