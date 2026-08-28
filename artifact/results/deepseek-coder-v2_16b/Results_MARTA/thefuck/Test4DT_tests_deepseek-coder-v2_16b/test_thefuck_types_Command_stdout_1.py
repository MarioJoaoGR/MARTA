
import pytest
from thefuck.types import Command

def test_invalid_inputs():
    with pytest.raises(TypeError):
        Command()  # This should raise TypeError because __init__ requires two arguments (script and output)
