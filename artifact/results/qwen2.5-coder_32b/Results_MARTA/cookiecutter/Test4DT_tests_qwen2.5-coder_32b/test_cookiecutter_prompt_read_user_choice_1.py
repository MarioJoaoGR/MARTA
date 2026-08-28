
import pytest
from unittest.mock import patch
from cookiecutter.prompt import read_user_choice


def test_valid_input_selects_correct_option():
    # Setup: Real instance with var_name='color' and options=['red', 'green', 'blue']
    var_name = 'color'
    options = ['red', 'green', 'blue']

    # Test valid input (selecting the second option)
    with patch('click.prompt', return_value='2'):
        selected_color_valid = read_user_choice(var_name, options)

    assert selected_color_valid == 'green'


