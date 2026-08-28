
import pytest
from unittest.mock import patch
from collections import OrderedDict
import click

# Import the function to be tested
from cookiecutter.prompt import read_user_choice

def test_read_user_choice_valid_input():
    options = ['red', 'blue', 'green']
    with patch('builtins.input', return_value='2'):
        result = read_user_choice('color', options)