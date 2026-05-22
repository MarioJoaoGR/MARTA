
import pytest
from httpie.downloads import trim_filename
import os

def test_invalid_input():
    with pytest.raises(TypeError):
        trim_filename(12345, "not an int")
