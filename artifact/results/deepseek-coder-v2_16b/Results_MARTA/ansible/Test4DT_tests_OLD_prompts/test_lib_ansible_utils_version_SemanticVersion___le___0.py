
import pytest
from ansible.utils.version import SemanticVersion


def test_invalid_inputs():
    with pytest.raises(ValueError):
        SemanticVersion('invalid_version')