
import pytest
from pathlib import Path
from httpie.sessions import Environment, Session

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # Test invalid input for 'path' parameter
        session = Session(
            path=42,  # Invalid type (should be Union[str, Path])
            env=Environment(),
            bound_host='example.com',
            session_id='unique_session_id'
        )
