
import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import get_hvcs
from typing import Optional

def get_token() -> Optional[str]:
    """
    Returns the token for the current VCS

    :return: The token in string form
    """
    return get_hvcs().token()

# Test scenarios

def test_none_configuration():
    with patch('semantic_release.hvcs.get_hvcs', return_value=None):
        assert get_token() is None
