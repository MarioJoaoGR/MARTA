
import pytest
from unittest.mock import patch
from ansible.module_utils.urls import UnixHTTPConnection


def test_invalid_input():
    with pytest.raises(TypeError):
        UnixHTTPConnection()