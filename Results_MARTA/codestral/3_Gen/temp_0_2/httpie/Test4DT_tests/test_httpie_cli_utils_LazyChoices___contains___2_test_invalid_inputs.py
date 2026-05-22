
import pytest
from httpie.cli.utils import LazyChoices

def test_invalid_inputs():
    with pytest.raises(TypeError):
        choices = LazyChoices(getter=lambda: [1, 2, 3])
