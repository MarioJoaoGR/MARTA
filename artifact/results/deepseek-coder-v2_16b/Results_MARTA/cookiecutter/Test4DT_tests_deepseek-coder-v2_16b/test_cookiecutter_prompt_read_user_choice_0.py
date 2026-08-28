
import pytest
from cookiecutter.prompt import read_user_choice


def test_invalid_input_for_choices():
    with pytest.raises(TypeError):
        read_user_choice('invalid_type', "not a list")

def test_empty_list_for_choices():
    with pytest.raises(ValueError):
        read_user_choice('empty', [])