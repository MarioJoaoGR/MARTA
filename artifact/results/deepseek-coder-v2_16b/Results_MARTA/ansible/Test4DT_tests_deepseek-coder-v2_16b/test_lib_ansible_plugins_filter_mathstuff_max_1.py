
import pytest
from ansible.plugins.filter import mathstuff


def test_valid_input_list():
    environment = {'result': None}
    result = mathstuff.max(environment, a=[1, 2, 3, 4])
    assert result == 4

def test_invalid_input_no_args():
    environment = {'result': None}
    with pytest.raises(TypeError):
        mathstuff.max(environment)