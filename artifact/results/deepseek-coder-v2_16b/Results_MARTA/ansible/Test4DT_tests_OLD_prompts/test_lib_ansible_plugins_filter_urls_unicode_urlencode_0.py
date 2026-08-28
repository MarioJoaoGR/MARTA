
import pytest
from ansible.plugins.filter.urls import unicode_urlencode

def test_invalid_input():
    with pytest.raises(TypeError):
        unicode_urlencode(None)
