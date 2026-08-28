
import pytest
from ansible.module_utils.compat.version import LooseVersion


def test_edge_case():
    version = LooseVersion(None)
    with pytest.raises(AttributeError):
        assert version.version == []