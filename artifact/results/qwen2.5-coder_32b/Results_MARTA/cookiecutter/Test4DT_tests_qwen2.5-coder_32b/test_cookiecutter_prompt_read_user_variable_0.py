
import pytest
from unittest.mock import patch
from cookiecutter.prompt import read_user_variable



def test_valid_input_accepted():
    # Test that a valid input is accepted and returned
    with patch('click.prompt', return_value='n'):
        enable_notifications = read_user_variable('Enable notifications? [y/n]', 'y')
        assert enable_notifications == 'n'

def test_empty_default_value_returned():
    # Test that an empty default value is returned when no input is provided
    with patch('click.prompt', return_value=''):
        username = read_user_variable('Enter your username:', '')
        assert username == ''

def test_non_empty_input_accepted():
    # Test that a non-empty input is accepted and returned
    with patch('click.prompt', return_value='john_doe'):
        username = read_user_variable('Enter your username:', 'default_user')
        assert username == 'john_doe'