
import pytest
from ansible.modules import pip

# Define a simple op_dict for testing purposes
op_dict = {
    'requests': True,
    'pytest': False,
}

def test_valid_package_name():
    assert pip._is_package_name("requests") == True
