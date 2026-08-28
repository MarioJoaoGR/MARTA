
import pytest
from unittest.mock import patch, MagicMock
import struct
from ansible.module_utils.connection import recv_data


def test_none_input():
    s = None
    with pytest.raises(AttributeError):
        result = recv_data(s)