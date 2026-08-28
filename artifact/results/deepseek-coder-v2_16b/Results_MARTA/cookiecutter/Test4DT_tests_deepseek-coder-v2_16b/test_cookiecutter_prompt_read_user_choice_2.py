
import pytest
from cookiecutter.prompt import read_user_choice


def test_invalid_options_type():
    with pytest.raises(TypeError):
        read_user_choice('invalid', "not a list")

def test_empty_options():
    with pytest.raises(ValueError):
        read_user_choice('empty', [])