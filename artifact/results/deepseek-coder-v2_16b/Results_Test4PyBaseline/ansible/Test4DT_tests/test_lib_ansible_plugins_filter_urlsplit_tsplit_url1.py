
import pytest
from ansible.plugins.filter import urlsplit as split_url_module
from ansible.errors import AnsibleFilterError

# Import the function using its module name
split_url = split_url_module.split_url

def test_split_url_basic():
    result = split_url('http://example.com/path?query=value#fragment')
    assert isinstance(result, dict), "Expected a dictionary but got {}".format(type(result))