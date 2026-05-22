
import pytest
from unittest.mock import patch
from httpie.internal.daemon_runner import _check_status

@pytest.fixture(scope="function")
def env():
    return {'STATUS_FILE': 'my_status_file'}

def test_missing_status_file(env):
    with patch('httpie.internal.daemon_runner._check_status'):
        _check_status(env)
