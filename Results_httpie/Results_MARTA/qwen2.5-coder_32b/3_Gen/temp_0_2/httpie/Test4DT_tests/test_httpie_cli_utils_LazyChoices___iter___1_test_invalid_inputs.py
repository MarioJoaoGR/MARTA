
import pytest
from httpie.cli.utils import LazyChoices
from typing import Callable, Iterable, Optional
from unittest.mock import patch

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test invalid getter type (non-callable)
        choices = LazyChoices(getter=5)
    
    with pytest.raises(TypeError):
        # Test invalid getter type (string instead of callable)
        choices = LazyChoices(getter='not_a_function')
