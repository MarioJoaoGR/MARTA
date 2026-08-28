
from lib.ansible.utils.version import SemanticVersion
import pytest


def test_invalid_input():
    with pytest.raises(ValueError):
        SemanticVersion("invalid-format")