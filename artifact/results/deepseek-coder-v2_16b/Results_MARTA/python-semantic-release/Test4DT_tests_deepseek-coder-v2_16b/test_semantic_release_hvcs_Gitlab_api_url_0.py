
import pytest
from unittest.mock import patch
from semantic_release.hvcs import Gitlab

def test_default_api_url():
    """Test default API URL when no configuration or environment variable is set."""
    with patch('semantic_release.hvcs.Gitlab.domain', return_value='gitlab.com'):
        assert Gitlab.api_url() == "https://gitlab.com"

