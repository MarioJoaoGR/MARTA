
import pytest
from superstring.superstring import SuperStringBase

def test_error_case_invalid_index():
    with pytest.raises(TypeError):
        obj = SuperStringBase('Hello', 'World!')
