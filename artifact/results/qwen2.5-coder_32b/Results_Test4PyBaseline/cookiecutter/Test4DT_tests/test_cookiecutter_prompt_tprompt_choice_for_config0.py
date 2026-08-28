
import pytest
from jinja2 import Environment
from cookiecutter.prompt import prompt_choice_for_config

def test_prompt_choice_for_config_no_input():
    env = Environment()
    context = {'project_name': 'Peanut Butter Cookie'}
    key = 'repo_name'
    options = ["{{ cookiecutter.project_name.replace(' ', '_') }}", "default_project"]
    
    selected_option = prompt_choice_for_config(context, env, key, options, no_input=True)
    assert selected_option == 'Peanut_Butter_Cookie'

def test_prompt_choice_for_config_single_option_no_input():
    env = Environment()
    context = {'project_name': 'Peanut Butter Cookie'}
    key = 'repo_name'
    options = ["{{ cookiecutter.project_name.replace(' ', '_') }}"]
    
    selected_option = prompt_choice_for_config(context, env, key, options, no_input=True)
    assert selected_option == 'Peanut_Butter_Cookie'

def test_prompt_choice_for_config_multiple_options_no_input():
    env = Environment()
    context = {'project_name': 'Peanut Butter Cookie'}
    key = 'repo_name'
    options = ["{{ cookiecutter.project_name.replace(' ', '_') }}", "default_project"]
    
    selected_option = prompt_choice_for_config(context, env, key, options, no_input=True)
    assert selected_option == 'Peanut_Butter_Cookie'

def test_prompt_choice_for_config_no_options():
    env = Environment()
    context = {'project_name': 'Peanut Butter Cookie'}
    key = 'repo_name'
    options = []
    
    with pytest.raises(ValueError):
        prompt_choice_for_config(context, env, key, options, no_input=True)

def test_prompt_choice_for_config_empty_string_option():
    env = Environment()
    context = {'project_name': 'Peanut Butter Cookie'}
    key = 'repo_name'
    options = ["", "default_project"]
    
    selected_option = prompt_choice_for_config(context, env, key, options, no_input=True)
    assert selected_option == ""

def test_prompt_choice_for_config_no_template():
    env = Environment()
    context = {'project_name': 'Peanut Butter Cookie'}
    key = 'repo_name'
    options = ["option1", "option2"]
    
    selected_option = prompt_choice_for_config(context, env, key, options, no_input=True)
    assert selected_option == "option1"
