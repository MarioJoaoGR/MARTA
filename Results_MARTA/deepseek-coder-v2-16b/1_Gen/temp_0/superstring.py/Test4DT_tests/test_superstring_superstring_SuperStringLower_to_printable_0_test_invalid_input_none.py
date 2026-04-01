
from superstring.superstring import SuperStringBase, SuperStringLower

def test_invalid_input_none():
    try:
        obj = SuperStringLower(SuperStringBase('Hello', 'World!'))
    except TypeError as e:
        assert str(e) == "SuperStringBase() takes no arguments"
