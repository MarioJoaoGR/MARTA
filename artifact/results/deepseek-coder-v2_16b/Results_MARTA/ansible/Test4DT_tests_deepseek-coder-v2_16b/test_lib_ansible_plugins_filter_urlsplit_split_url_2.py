
import pytest
from ansible.plugins.filter import urlsplit
from ansible.errors import AnsibleFilterError

# Assuming 'helpers' is a module that should be mocked or imported correctly
# However, since it's not defined in the provided code snippet, we will focus on testing the function itself


def test_specific_component_query():
    result = urlsplit.split_url('http://example.com/path?query=value#fragment', 'netloc')
    assert result == 'example.com'

def test_unknown_component_query():
    with pytest.raises(AnsibleFilterError):
        urlsplit.split_url('http://example.com/path?query=value#fragment', 'unknown_component')