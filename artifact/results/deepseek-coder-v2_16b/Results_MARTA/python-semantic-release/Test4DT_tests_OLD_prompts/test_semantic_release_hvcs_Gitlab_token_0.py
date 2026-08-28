
import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import Gitlab

def test_gitlab_token_retrieval():
    with patch('os.environ', {'GL_TOKEN': 'test_token'}):
        token = Gitlab.token()
        assert token == 'test_token'

def test_gitlab_token_not_set():
    with patch('os.environ', {}):
        token = Gitlab.token()
        assert token is None
