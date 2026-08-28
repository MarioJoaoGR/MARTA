
import pytest
from ansible.utils.unsafe_proxy import to_unsafe_bytes



def test_invalid_input_1():
    with pytest.raises(TypeError):
        to_unsafe_bytes()