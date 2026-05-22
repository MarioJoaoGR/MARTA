
import pytest
from httpie.cli.utils import LazyChoices

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test invalid input by passing a non-callable object as getter
        LazyChoices(getter=42)  # Assuming 42 is an example of an invalid input
