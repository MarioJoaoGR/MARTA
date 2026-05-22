
import pytest
from httpie.context import Environment

def test_valid_inputs():
    env = Environment()
    with pytest.raises(AssertionError):
        assert callable(env.rich_error_console)
