
import pytest
from unittest.mock import patch, MagicMock
from httpie.context import Environment

@pytest.fixture(scope="function")
def setup_environment():
    with patch('httpie.context.sys.stdin', new=MagicMock()):
        with patch('httpie.context.sys.stdout', new=MagicMock()):
            with patch('httpie.context.sys.stderr', new=MagicMock()):
                env = Environment()
                yield env

def test_valid_inputs(setup_environment):
    env = setup_environment
    assert isinstance(env, Environment)
