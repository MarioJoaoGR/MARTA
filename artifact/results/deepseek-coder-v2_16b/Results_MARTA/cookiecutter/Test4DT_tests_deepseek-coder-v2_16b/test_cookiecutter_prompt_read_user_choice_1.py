
import pytest
from cookiecutter.prompt import read_user_choice


def test_invalid_type():
    with pytest.raises(TypeError):
        read_user_choice('invalid', None)

def test_empty_list():
    with pytest.raises(ValueError):
        read_user_choice('empty', [])