
import pytest
from isort._vendored.tomli._parser import skip_chars

def test_error_handling():
    with pytest.raises(TypeError):
        skip_chars("valid string", "invalid type", ["a"])
