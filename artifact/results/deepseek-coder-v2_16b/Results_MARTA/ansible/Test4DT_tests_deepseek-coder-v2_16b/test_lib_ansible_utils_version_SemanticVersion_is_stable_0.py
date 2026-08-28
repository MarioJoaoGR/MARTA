
import pytest
from ansible.utils.version import SemanticVersion


def test_edge_cases():
    with pytest.raises(ValueError):
        SemanticVersion('invalid-version')