
import pytest
from ansible.modules.pip import _is_package_name

# Define a simple dictionary to simulate op_dict for testing purposes
op_dict = {
    'requests': None,
    'pytest': None,
    # Add other potential package names here if needed
}

def test_valid_package_name():
    assert _is_package_name("requests") == True
