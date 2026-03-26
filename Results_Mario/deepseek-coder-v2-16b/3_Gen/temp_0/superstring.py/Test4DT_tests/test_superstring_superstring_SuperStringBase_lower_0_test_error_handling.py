
import pytest
from superstring.superstring import SuperStringBase, SUPERSTRING_MINIMAL_LENGTH

def test_error_handling():
    with pytest.raises(TypeError):
        base_string = SuperStringBase('short')
