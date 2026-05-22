
import pytest
from unittest.mock import patch, MagicMock
from httpie.cli.utils import LazyChoices

def test_invalid_inputs():
    with pytest.raises(TypeError):
        choices = LazyChoices(getter='not a callable', help_formatter=lambda x, y: str(x))
