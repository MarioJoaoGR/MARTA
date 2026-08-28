
import pytest
from ansible.module_utils.common.collections import ImmutableDict

def test_edge_case():
    with pytest.raises(TypeError):
        ImmutableDict(None)
