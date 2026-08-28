
import pytest
from ansible.errors import AnsibleFilterError
import hashlib
from six import text_type, binary_type

def to_bytes(text, errors='surrogate_or_strict'):
    if isinstance(text, binary_type):
        return text
    elif isinstance(text, text_type):
        return text.encode(errors=errors)
    else:
        raise TypeError("to_bytes must be called with a string type")

def get_hash(data, hashtype='sha1'):
    try:
        h = hashlib.new(hashtype)
    except Exception as e:
        # hash is not supported?
        raise AnsibleFilterError(e)

    h.update(to_bytes(data, errors='surrogate_or_strict'))
    return h.hexdigest()

# Test cases for get_hash function


def test_invalid_hashtype():
    data = 'hello world'
    hashtype = 'unknown_hash'
    with pytest.raises(AnsibleFilterError):
        get_hash(data, hashtype)