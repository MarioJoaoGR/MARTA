
import pytest
from isort.sorting import Config, sort

def test_invalid_input():
    with pytest.raises(TypeError):
        config = Config()
