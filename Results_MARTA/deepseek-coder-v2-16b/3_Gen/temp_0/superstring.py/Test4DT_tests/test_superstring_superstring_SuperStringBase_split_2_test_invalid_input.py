
import pytest
from unittest.mock import patch, MagicMock
from superstring.superstring import SuperStringBase

def test_invalid_input():
    with pytest.raises(TypeError):
        invalid_string = SuperStringBase(None)
