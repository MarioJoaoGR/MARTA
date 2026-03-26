
import pytest
import os
from pytutils.env import expand

# Test case for expanding a user home directory placeholder
def test_expand_home_directory():
    expected_output = os.path.expanduser("~/Documents")
    assert expand("~/Documents") == expected_output

# Test case for setting environment variables and expanding them in the string
@pytest.mark.skipif(not 'USER' in os.environ or not 'HOME' in os.environ, reason="Environment variables USER and HOME must be set to run this test")
def test_expand_with_env_vars():
    os.environ['USER'] = 'admin'
    os.environ['HOME'] = '/root'
    expected_output = os.path.expanduser("~") + "/Desktop"