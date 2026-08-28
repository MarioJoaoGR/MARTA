
import pytest
from unittest.mock import patch
from semantic_release.hvcs import Github, TokenAuth

def test_github_auth_with_env_var():
    """Test when GH_TOKEN environment variable is set"""
    with patch.dict('os.environ', {'GH_TOKEN': 'fake_token'}):
        auth = Github.auth()
        assert isinstance(auth, TokenAuth)
