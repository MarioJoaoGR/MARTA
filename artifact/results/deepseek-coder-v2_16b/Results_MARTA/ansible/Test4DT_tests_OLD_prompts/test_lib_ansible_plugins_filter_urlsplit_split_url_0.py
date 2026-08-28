
import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter import urlsplit



def test_unknown_component_query():
    with pytest.raises(AnsibleFilterError):
        urlsplit.split_url('http://example.com/path?query=value#fragment', query='unknown_component')