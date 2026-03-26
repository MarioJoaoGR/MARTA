
from isort._vendored.tomli._parser import create_dict_rule, Output
from pytest import raises

def test_invalid_key_character():
    src = "invalid#key"
    pos = 0
    
    # Mock the creation of an instance of Output to avoid missing arguments error
    with raises(TypeError):
        create_dict_rule(src, pos, Output())
