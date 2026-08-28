
import pytest
from ansible.plugins.shell.powershell import _parse_clixml
import xml.etree.ElementTree as ET
import re

def to_bytes(s):
    if isinstance(s, str):
        return s.encode('latin-1')
    assert isinstance(s, bytes), "to_bytes expects a bytes or string argument"
    return s

@pytest.fixture(params=[b'#< CLIXML...\n<Objs...', b'Invalid XML...'])
def data(request):
    return request.param

def test_valid_input_happy_path(data):
    result = _parse_clixml(data)
    assert isinstance(result, bytes), "Expected a byte string"
    assert len(result) > 0, "Expected non-empty byte string"

def test_none_input():
    with pytest.raises(TypeError):
        _parse_clixml(None)

def test_invalid_clixml(data):
    result = _parse_clixml(data)
    assert isinstance(result, bytes), "Expected a byte string"
    assert len(result) == 0, "Expected empty byte string for invalid CLIXML data"
