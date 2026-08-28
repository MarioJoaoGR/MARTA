
import pytest
from ansible.executor.powershell.module_manifest import _slurp
from ansible.errors import AnsibleError
import os

def test_slurp_existing_file():
    # Test reading an existing file
    path = 'example.txt'
    with open(path, 'wb') as f:
        f.write(b"test content")
    try:
        data = _slurp(path)
        assert data == b"test content"
    finally:
        os.remove(path)

def test_slurp_nonexistent_file():
    # Test handling a non-existent file
    path = 'nonexistent.txt'
    with pytest.raises(AnsibleError) as excinfo:
        _slurp(path)
    assert str(excinfo.value) == "imported module support code does not exist at %s" % os.path.abspath(path)

def test_slurp_binary_file():
    # Test reading a binary file
    path = 'binaryfile.bin'
    with open(path, 'wb') as f:
        f.write(b"\x01\x02\x03")
    try:
        data = _slurp(path)
        assert data == b"\x01\x02\x03"
    finally:
        os.remove(path)
