
from isort._vendored.tomli._parser import create_dict_rule, Output, Pos
from pytest import raises

def test_create_dict_rule():
    src = "name = 'value'"
    pos = Pos(0)
    
    # Assuming the Output class has a constructor that takes two arguments: data and flags.
    with raises(TypeError) as excinfo:
        create_dict_rule(src, pos, Output())
    assert str(excinfo.value) == "Output.__new__() missing 2 required positional arguments: 'data' and 'flags'"
