
import pytest
from unittest.mock import patch, MagicMock
from jinja2 import Environment
from cookiecutter.prompt import render_variable

# Test for valid input with basic template
def test_valid_input_basic_template():
    env = Environment()
    cookiecutter_dict = {'project_name': 'Peanut Butter Cookie'}
    raw = '{{ cookiecutter.project_name.replace(" ", "_") }}'
    expected_output = 'Peanut_Butter_Cookie'
    
    with patch('jinja2.Environment') as mock_env:
        mock_env.return_value = env
        assert render_variable(env, raw, cookiecutter_dict) == expected_output

# Test for valid input with nested dictionary
def test_valid_input_nested_dictionary():
    env = Environment()
    cookiecutter_dict = {'var1': 'value1', 'var2': 'value2'}
    raw_dict = {
        'key1': '{{ cookiecutter.var1 }}',
        'key2': '{{ cookiecutter.var2 }}'
    }
    expected_output_dict = {'key1': 'value1', 'key2': 'value2'}
    
    with patch('jinja2.Environment') as mock_env:
        mock_env.return_value = env
        assert render_variable(env, raw_dict, cookiecutter_dict) == expected_output_dict

# Test for invalid input (None)
def test_invalid_input_none():
    env = Environment()
    cookiecutter_dict = {}
    raw = None
    expected_output = None
    
    with patch('jinja2.Environment') as mock_env:
        mock_env.return_value = env
        assert render_variable(env, raw, cookiecutter_dict) == expected_output
