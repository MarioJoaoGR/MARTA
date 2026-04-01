
import pytest

from isort._vendored.tomli._parser import Key, Output, Pos, create_dict_rule


def test_invalid_input():
    src = "table [key1.key2] value"
    pos = Pos(0)
    
    # Mock the Output class to return a new instance with predefined data and flags
    with pytest.raises(TypeError):  # Expecting a TypeError due to missing arguments
        create_dict_rule(src, pos, Output())
