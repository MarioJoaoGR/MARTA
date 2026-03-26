
import pytest
from superstring.superstring import SuperStringBase

def test_invalid_input():
    with pytest.raises(TypeError):
        s3 = SuperStringBase(123)
