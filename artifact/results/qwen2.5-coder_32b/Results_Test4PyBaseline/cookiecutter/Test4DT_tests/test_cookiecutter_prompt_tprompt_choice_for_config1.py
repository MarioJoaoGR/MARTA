
import pytest
from unittest.mock import patch, MagicMock
from jinja2 import Environment
from cookiecutter.prompt import prompt_choice_for_config

# Mocking read_user_choice to simulate user input
@patch('cookiecutter.prompt.read_user_choice')
def test_prompt_choice_for_config_single_option_with_input(mock_read_user_choice):
    env = Environment()
    context = {'project_name': 'Peanut Butter Cookie'}
    key = 'repo_name'
    options = ["{{ cookiecutter.project_name.replace(' ', '_') }}"]
    
    # Mock the return value of read_user_choice
    mock_read_user_choice.return_value = "Peanut_Butter_Cookie"
    
    selected_option = prompt_choice_for_config(context, env, key, options, no_input=False)
    assert selected_option == "Peanut_Butter_Cookie"
    mock_read_user_choice.assert_called_once_with(key, ["Peanut_Butter_Cookie"], None, '')

@patch('cookiecutter.prompt.read_user_choice')
def test_prompt_choice_for_config_multiple_options_with_input(mock_read_user_choice):
    env = Environment()
    context = {'project_name': 'Peanut Butter Cookie'}
    key = 'repo_name'
    options = ["{{ cookiecutter.project_name.replace(' ', '_') }}", "default_project"]
    
    # Mock the return value of read_user_choice
    mock_read_user_choice.return_value = "default_project"
    
    selected_option = prompt_choice_for_config(context, env, key, options, no_input=False)
    assert selected_option == "default_project"
    mock_read_user_choice.assert_called_once_with(key, ["Peanut_Butter_Cookie", "default_project"], None, '')

@patch('cookiecutter.prompt.read_user_choice')
def test_prompt_choice_for_config_no_template_with_input(mock_read_user_choice):
    env = Environment()
    context = {'project_name': 'Peanut Butter Cookie'}
    key = 'repo_name'
    options = ["option1", "option2"]
    
    # Mock the return value of read_user_choice
    mock_read_user_choice.return_value = "option2"
    
    selected_option = prompt_choice_for_config(context, env, key, options, no_input=False)
    assert selected_option == "option2"
    mock_read_user_choice.assert_called_once_with(key, ["option1", "option2"], None, '')

@patch('cookiecutter.prompt.read_user_choice')
def test_prompt_choice_for_config_empty_string_option_with_input(mock_read_user_choice):
    env = Environment()
    context = {'project_name': 'Peanut Butter Cookie'}
    key = 'repo_name'
    options = ["", "default_project"]
    
    # Mock the return value of read_user_choice
    mock_read_user_choice.return_value = ""
    
    selected_option = prompt_choice_for_config(context, env, key, options, no_input=False)
    assert selected_option == ""
    mock_read_user_choice.assert_called_once_with(key, ["", "default_project"], None, '')
