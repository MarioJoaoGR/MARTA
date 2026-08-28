
import pytest
from unittest.mock import patch
from ansible.utils.version import SemanticVersion


def test_invalid_case():
    with pytest.raises(ValueError):
        SemanticVersion("invalid-version")

def test_comparison_equal():
    v1 = SemanticVersion("1.0.0")
    v2 = SemanticVersion("1.0.0")
    assert v1 == v2

def test_comparison_greater():
    v1 = SemanticVersion("2.0.0")
    v2 = SemanticVersion("1.99.99")
    assert v1 > v2

def test_comparison_lesser():
    v1 = SemanticVersion("1.0.0-alpha")
    v2 = SemanticVersion("2.0.0-beta")
    assert v1 < v2