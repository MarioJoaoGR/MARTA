
import pytest
from unittest.mock import patch, MagicMock
from superstring.superstring import SuperStringBase

def test_invalid_strip():
    with pytest.raises(TypeError):
        obj = SuperStringBase(None)
        obj.strip()
