
import pytest
from semantic_release.hvcs import Github
import os
from unittest.mock import patch

def test_github_token():
    with patch.dict(os.environ, {"GH_TOKEN": "fake_token"}):
        assert Github.token() == "fake_token"

def test_github_default_domain():
    assert Github.DEFAULT_DOMAIN == 'github.com'
