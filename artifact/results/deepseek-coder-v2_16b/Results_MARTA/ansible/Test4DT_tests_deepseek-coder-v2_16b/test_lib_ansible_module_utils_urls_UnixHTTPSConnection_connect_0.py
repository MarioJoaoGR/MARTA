
import pytest
from ansible.module_utils.urls import UnixHTTPSConnection



def test_invalid_input():
    with pytest.raises(TypeError):
        UnixHTTPSConnection()