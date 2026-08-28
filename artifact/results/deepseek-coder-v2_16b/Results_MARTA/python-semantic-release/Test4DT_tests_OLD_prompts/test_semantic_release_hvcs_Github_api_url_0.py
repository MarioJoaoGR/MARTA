
import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import Github

def test_api_url_default_domain():
    with patch('semantic_release.hvcs.config', {'hvcs_domain': None}):
        assert Github().api_url() == 'https://api.github.com'

def test_api_url_custom_domain():
    with patch('semantic_release.hvcs.config', {'hvcs_domain': 'customdomain.com'}):
        assert Github().api_url() == 'https://customdomain.com'
