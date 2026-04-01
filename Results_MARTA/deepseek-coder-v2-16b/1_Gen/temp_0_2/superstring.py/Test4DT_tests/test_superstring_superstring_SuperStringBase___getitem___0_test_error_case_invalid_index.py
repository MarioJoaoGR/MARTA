
import pytest
from superstring.superstring import SuperStringBase

def test_error_case_invalid_index():
    with pytest.raises(TypeError):
        super_string = SuperStringBase('Hello, World!')
        assert False, "SuperStringBase() takes no arguments"
