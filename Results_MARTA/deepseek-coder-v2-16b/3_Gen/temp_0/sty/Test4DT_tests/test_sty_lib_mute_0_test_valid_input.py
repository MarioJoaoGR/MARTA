
import pytest
from unittest.mock import Mock
from sty.lib import mute, Register

@pytest.fixture
def valid_objects():
    register1 = Mock(spec=Register)
    register2 = Mock(spec=Register)
    return [register1, register2]

def test_valid_input(valid_objects):
    for obj in valid_objects:
        mute(obj)
