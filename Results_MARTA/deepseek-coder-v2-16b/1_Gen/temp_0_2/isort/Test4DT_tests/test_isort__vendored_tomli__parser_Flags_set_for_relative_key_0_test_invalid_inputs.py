
import pytest
from isort._vendored.tomli._parser import Flags

def test_invalid_inputs():
    flags = Flags()
    
    # Test raising errors for invalid inputs
    with pytest.raises(TypeError):
        flags.set_for_relative_key("a", 1, Flags.EXPLICIT_NEST)  # head_key should be a sequence
    with pytest.raises(TypeError):
        flags.set_for_relative_key(None, "b", Flags.EXPLICIT_NEST)  # head_key should not be None
