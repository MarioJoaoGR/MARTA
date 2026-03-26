
from superstring.superstring import SuperStringBase, SuperStringLower

def test_invalid_input_empty():
    try:
        obj = SuperStringLower(SuperStringBase('Hello', 'World!'))
        assert False, "Expected TypeError but passed"
    except TypeError as e:
        assert str(e) == "SuperStringBase() takes no arguments", f"Unexpected error message: {str(e)}"
