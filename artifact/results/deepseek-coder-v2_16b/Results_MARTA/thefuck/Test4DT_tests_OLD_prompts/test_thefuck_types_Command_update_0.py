
import pytest
from thefuck.types import Command

def test_invalid_input():
    with pytest.raises(TypeError):
        Command()
