
import pytest
from unittest.mock import patch
from ansible.utils.version import SemanticVersion


def test_invalid_input():
    with pytest.raises(ValueError):
        SemanticVersion("invalid-format")

def test_version_comparison_greater():
    v1 = SemanticVersion("2.0.0-alpha")
    v2 = SemanticVersion("1.99.99")
    assert (v1 > v2) == True

def test_version_comparison_equal():
    v1 = SemanticVersion("1.0.0-beta")
    v2 = SemanticVersion("1.0.0-beta")
    assert (v1 == v2) == True

def test_version_comparison_lesser():
    v1 = SemanticVersion("1.0.0-gamma")
    v2 = SemanticVersion("2.0.0-delta")
    assert (v1 < v2) == True