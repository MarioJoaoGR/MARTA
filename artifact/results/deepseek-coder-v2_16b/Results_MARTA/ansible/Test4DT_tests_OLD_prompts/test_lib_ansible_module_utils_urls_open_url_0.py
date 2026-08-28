
import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.urls import open_url

def test_open_url_with_none_url():
    with pytest.raises(TypeError):
        open_url(None)
