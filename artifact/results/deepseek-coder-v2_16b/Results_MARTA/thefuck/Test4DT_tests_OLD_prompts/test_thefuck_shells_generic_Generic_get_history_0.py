
import pytest
from unittest.mock import patch, MagicMock
from thefuck.shells.generic import Generic


def test_invalid_input():
    with pytest.raises(TypeError):
        Generic().get_history('unexpected_argument')