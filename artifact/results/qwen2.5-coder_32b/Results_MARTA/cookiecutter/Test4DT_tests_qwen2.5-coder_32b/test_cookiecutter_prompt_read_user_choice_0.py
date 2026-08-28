
import pytest
from unittest.mock import patch
from cookiecutter.prompt import read_user_choice


def test_valid_input_selection():
    options = ['apple', 'banana', 'cherry']
    with patch('click.prompt', return_value='2'):
        selected_fruit = read_user_choice('fruit', options)
    assert selected_fruit == 'banana'
