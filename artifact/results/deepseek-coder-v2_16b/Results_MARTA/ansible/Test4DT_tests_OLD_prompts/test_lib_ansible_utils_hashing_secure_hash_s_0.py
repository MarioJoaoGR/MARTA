
import pytest
from ansible.utils.hashing import secure_hash_s
import hashlib



def test_invalid_input():
    with pytest.raises(TypeError):
        secure_hash_s("hello world", "not_a_hash_function")