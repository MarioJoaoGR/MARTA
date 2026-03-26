# Module: pymonet.box
import pytest
from pymonet.box import Box
from pymonet.monad_try import Try

# Test creating a Box with an integer value
def test_create_box_with_int():
    box = Box(42)
    assert box.value == 42

# Test creating a Box with a string value
def test_create_box_with_string():
    box = Box("Hello, World!")
    assert box.value == "Hello, World!"

# Test transforming into a Try monad
def test_to_try():
    box = Box("Hello")
    try_monad = box.to_try()
    assert isinstance(try_monad, Try)
    assert try_monad.is_success is True
    assert try_monad.value == "Hello"

# Test transforming into a Try monad with an exception (not applicable in this case since it's always successful)
def test_to_try_exception():
    # This would be more relevant if the to_try method had potential exceptions
    pass

if __name__ == "__main__":
    pytest.main()
