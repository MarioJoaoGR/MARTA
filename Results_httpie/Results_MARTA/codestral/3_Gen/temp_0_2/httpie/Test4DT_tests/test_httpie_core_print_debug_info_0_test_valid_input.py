
import pytest
from unittest.mock import patch, MagicMock
from httpie.core import print_debug_info

@pytest.fixture
def env():
    return MagicMock()

@pytest.mark.parametrize("httpie_version, requests_version, pygments_version", [
    ("2.0.0", "2.25.1", "2.7.4"),
])
def test_valid_input(env, httpie_version, requests_version, pygments_version):
    with patch('httpie.core.httpie_version', httpie_version):
        with patch('httpie.core.requests_version', requests_version):
            with patch('httpie.core.pygments_version', pygments_version):
                print_debug_info(env)
                
                # Add assertions to check the output or behavior if needed
