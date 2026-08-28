
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.filter.mathstuff import unique

def union(environment, a, b):
    if isinstance(a, (list, set)) and isinstance(b, (list, set)):
        return list(set(a) | set(b))
    else:
        return unique(environment, list(set([*a, *b])))


def test_invalid_inputs():
    with patch('ansible.plugins.filter.mathstuff.unique', side_effect=TypeError):
        with pytest.raises(TypeError):
            union({'var': 'value'}, None, None)