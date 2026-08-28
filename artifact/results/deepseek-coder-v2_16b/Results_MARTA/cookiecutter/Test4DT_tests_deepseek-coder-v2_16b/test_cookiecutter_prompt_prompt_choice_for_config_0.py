
import pytest
from cookiecutter.prompt import prompt_choice_for_config
from jinja2 import Environment


def test_no_input():
    cookiecutter_dict = {'project_name': 'Peanut Butter Cookie', 'other_key': 'value'}
    env = Environment()
    key = 'project_name'
    options = ['Peanut Butter Cookie', 'Chocolate Chip Cookie']
    
    result = prompt_choice_for_config(cookiecutter_dict, env, key, options, no_input=True)
    
    assert isinstance(result, str), "Expected a string but got something else"
    assert result == cookiecutter_dict['project_name'], f"Expected {cookiecutter_dict['project_name']} but got {result}"