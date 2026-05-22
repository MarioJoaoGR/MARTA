
import pytest
from unittest.mock import patch
from httpie.cli.argtypes import SessionNameValidator

def test_none_input():
    validator = SessionNameValidator('Invalid session name')
    
    with pytest.raises(TypeError):
        validator(None)
