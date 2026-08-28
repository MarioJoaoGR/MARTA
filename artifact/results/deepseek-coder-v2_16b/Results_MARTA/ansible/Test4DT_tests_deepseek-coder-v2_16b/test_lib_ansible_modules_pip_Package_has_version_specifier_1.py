
import pytest
from your_module_name import Package  # Replace 'your_module_name' with the actual module name where Package is defined

# Test Scenario 1: Test standard input with version specified
def test_valid_case_with_version():
    pkg = Package('requests', '2.25.1')
    assert pkg.package_name == 'requests'
    assert pkg._requirement.project_name == 'requests'
    assert not hasattr(pkg, '_plain_package')  # This should be set internally by the class

# Test Scenario 2: Test edge case without specifying a version
def test_edge_case_no_version():
    pkg = Package('setuptools')
    assert pkg.package_name == 'setuptools'
    assert not hasattr(pkg, '_requirement')  # This should be set internally by the class

# Test Scenario 3: Test invalid input that should raise ValueError
def test_invalid_input():
    with pytest.raises(ValueError):
        pkg = Package('invalid-package', 'invalid-version')
