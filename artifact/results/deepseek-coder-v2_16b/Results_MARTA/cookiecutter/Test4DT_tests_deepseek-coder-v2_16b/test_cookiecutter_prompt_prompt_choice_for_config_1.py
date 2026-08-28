
import pytest
from cookiecutter.prompt import prompt_choice_for_config
from jinja2 import Environment


def test_prompt_choice_for_config_with_no_input():
    cookiecutter_dict = {'project_name': 'Peanut Butter Cookie', 'other_config': 'value'}
    env = Environment()
    key = 'project_name'
    options = ['Peanut Butter Cookie', 'Chocolate Chip Cookie']
    no_input = True
    
    result = prompt_choice_for_config(cookiecutter_dict, env, key, options, no_input)
    
    assert isinstance(result, str), "Expected a string but got something else."
    assert result == 'Peanut Butter Cookie', f"Expected 'Peanut Butter Cookie' but got {result}."