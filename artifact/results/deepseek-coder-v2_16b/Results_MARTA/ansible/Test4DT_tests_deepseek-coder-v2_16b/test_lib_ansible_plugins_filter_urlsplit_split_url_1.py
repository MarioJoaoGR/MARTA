
import pytest
from ansible.plugins.filter import urlsplit
from ansible.errors import AnsibleFilterError


def test_split_url_specific_component():
    result = urlsplit.split_url('http://example.com/path?query=value#fragment', 'netloc')
    assert result == 'example.com'


def test_split_url_unknown_component():
    with pytest.raises(AnsibleFilterError):
        urlsplit.split_url('http://example.com/path?query=value#fragment', 'unknown_component')