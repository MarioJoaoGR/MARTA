
import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import Gitlab

def test_domain_with_config():
    with patch('semantic_release.hvcs.config', {'hvcs_domain': 'my-custom-gitlab'}):
        assert Gitlab.domain() == 'my-custom-gitlab'

def test_domain_with_env_var():
    with patch('os.environ', {'CI_SERVER_HOST': 'private-gitlab.example.com'}):
        assert Gitlab.domain() == 'private-gitlab.example.com'

def test_default_to_gitlab_com():
    with patch('semantic_release.hvcs.config', {}):
        with patch('os.environ', {'CI_SERVER_HOST': ''}):
            assert Gitlab.domain() == 'gitlab.com'
