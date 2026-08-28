
import pytest
import io
import hashlib
from ansible.cli.scripts import ansible_connection_cli_stub

def to_text(data):
    return data.decode('utf-8') if isinstance(data, bytes) else data


def test_invalid_input():
    byte_stream = io.BufferedReader(io.BytesIO(b'some binary data'))
    
    with pytest.raises(Exception):
        ansible_connection_cli_stub.read_stream(byte_stream)