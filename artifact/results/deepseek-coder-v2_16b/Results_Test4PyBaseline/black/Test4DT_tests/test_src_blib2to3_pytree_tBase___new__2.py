# Module: blib2to3.pytree
# Import the function properly using the provided module name.
from blib2to3.pytree import Base

def test_base_instantiation():
    try:
        base = Base()
        assert False, "Expected AssertionError when trying to instantiate Base"
    except AssertionError as e:
        assert str(e) == "Cannot instantiate Base", f"Unexpected error message: {str(e)}"

# Test case for ensuring the constructor prevents instantiation of Base.
def test_base_constructor():
    try:
        base = Base()
        assert False, "Expected AssertionError when trying to instantiate Base"
    except AssertionError as e:
        assert str(e) == "Cannot instantiate Base", f"Unexpected error message: {str(e)}"
