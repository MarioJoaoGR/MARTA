
import pytest
from unittest.mock import patch, MagicMock
from httpie.config import BaseConfigDict

def test_invalid_input():
    with pytest.raises(TypeError):
        with patch('httpie.config.BaseConfigDict.__name__', new=MagicMock(return_value='BaseConfigDict')):
            pass
