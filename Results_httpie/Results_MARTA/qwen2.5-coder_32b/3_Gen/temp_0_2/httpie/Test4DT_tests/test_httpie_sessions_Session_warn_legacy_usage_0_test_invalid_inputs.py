
import pytest
from pathlib import Path
from httpie.sessions import Session, Environment

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test invalid type for 'path' parameter
        Session(path=42, env=Environment(), bound_host='example.com', session_id='unique_id')
