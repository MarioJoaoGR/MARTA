
import pytest
from unittest.mock import Mock, patch
from httpie.cli.utils import LazyChoices

def test_invalid_input():
    with pytest.raises(TypeError):
        # Test invalid getter type (should raise TypeError)
        choices = LazyChoices(getter=lambda: 'not a callable', sort=False, cache=True)
