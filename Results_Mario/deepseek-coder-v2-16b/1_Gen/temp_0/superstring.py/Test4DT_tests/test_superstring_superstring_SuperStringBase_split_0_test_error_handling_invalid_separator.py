
import pytest
from superstring.superstring import SuperStringBase

def test_error_handling_invalid_separator():
    with pytest.raises(TypeError):
        s = SuperStringBase("Hello, World!")  # This should not be called directly in the test function
