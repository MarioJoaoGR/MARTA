
import pytest
from ansible.config.manager import _get_entry


def test_edge_cases():
    with pytest.raises(TypeError):
        _get_entry()