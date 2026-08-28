
import pytest
from unittest.mock import patch
from ansible.plugins.filter.core import extract as core_extract



def test_invalid_inputs():
    data = None
    item = 'a'
    container = {'a': {'b': {'c': 1}}}
    with patch('ansible.plugins.filter.core.extract', side_effect=lambda x, y: x[y]):
        with pytest.raises(AttributeError):
            core_extract(container, item, container=data)