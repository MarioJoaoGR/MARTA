
import pytest
from ansible.utils.version import SemanticVersion


def test_invalid_input_error_handling():
    with pytest.raises(ValueError):
        SemanticVersion("invalid-version")