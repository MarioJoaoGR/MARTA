
import pytest
from ansible.utils.version import SemanticVersion

def test_invalid_input_error_handling():
    try:
        v5 = SemanticVersion('invalid-format')
    except ValueError as e:
        assert str(e) == "invalid semantic version 'invalid-format'"
