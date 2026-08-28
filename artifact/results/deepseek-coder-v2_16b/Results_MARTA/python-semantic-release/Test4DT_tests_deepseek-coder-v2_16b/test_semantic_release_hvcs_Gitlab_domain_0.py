
import pytest
from unittest.mock import patch
import os
from semantic_release.hvcs import Gitlab

def test_valid_env_var():
    with patch.dict('os.environ', {'CI_SERVER_HOST': 'private-gitlab.example.com'}):
        assert Gitlab.domain() == "private-gitlab.example.com"

def test_default_case():
    # Remove the CI_SERVER_HOST environment variable to trigger the default case
    with patch.dict('os.environ', {}, clear=True):
        assert Gitlab.domain() == "gitlab.com"

def test_config_fallback():
    # Mock config to not have "hvcs_domain" set, triggering fallback to environment variable
    with patch('semantic_release.hvcs.config', {'hvcs_domain': None}):
        assert Gitlab.domain() == "gitlab.com"
