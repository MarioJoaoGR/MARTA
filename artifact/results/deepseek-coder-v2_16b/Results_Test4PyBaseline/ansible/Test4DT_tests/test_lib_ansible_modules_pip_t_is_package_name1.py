
import pytest
from ansible.modules.pip import _is_package_name

# Assuming op_dict is defined and contains relevant keys for testing
op_dict = {
    '1': None,
    '2': None,
    '3': None,
    # Add other potential version specifiers as keys in this dictionary
}

def test__is_package_name():
    # Test a valid package name
    assert _is_package_name("requests") == True
    
    # Test an invalid version specifier