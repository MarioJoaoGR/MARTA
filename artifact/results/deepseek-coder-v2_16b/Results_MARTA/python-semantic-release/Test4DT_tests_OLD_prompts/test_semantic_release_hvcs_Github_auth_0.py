
import pytest
from unittest.mock import patch
import os
from semantic_release.hvcs import Github, TokenAuth

def test_valid_token():
    with patch.dict(os.environ, {'GH_TOKEN': 'valid_token'}):
        auth = Github.auth()
        assert isinstance(auth, TokenAuth), "Expected TokenAuth instance but got a different type"

def test_invalid_token():
    with patch.dict(os.environ, {'GH_TOKEN': ''}):
        auth = Github.auth()
        assert auth is None, "Expected None but got an authentication instance"
