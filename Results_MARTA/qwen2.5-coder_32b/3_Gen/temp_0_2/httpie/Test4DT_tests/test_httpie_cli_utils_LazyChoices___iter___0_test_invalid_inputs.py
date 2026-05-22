
import pytest
from unittest.mock import patch
from httpie.cli.utils import LazyChoices
from typing import Callable, Iterable, Optional

def test_invalid_inputs():
    with pytest.raises(TypeError):
        choices = LazyChoices(getter=5)
