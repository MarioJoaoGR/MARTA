
import pytest
from jinja2 import Environment
from cookiecutter.prompt import prompt_choice_for_config



def test_single_option_no_input():
    # Case 3: Single option provided and no_input is True
    cookiecutter_dict = {'project_name': 'Peanut Butter Cookie'}
    env = Environment()
    key = 'base_template'
    options = ["{{ cookiecutter.project_name.replace(' ', '_') }}_template"]
    no_input = True

    selected_option = prompt_choice_for_config(cookiecutter_dict, env, key, options, no_input)
    assert selected_option == "Peanut_Butter_Cookie_template"

def test_multiple_options_no_input():
    # Case 4: Multiple options provided and no_input is True
    cookiecutter_dict = {'project_name': 'Chocolate Chip Cookie'}
    env = Environment()
    key = 'base_template'
    options = ["{{ cookiecutter.project_name.replace(' ', '_') }}_template", 'default_template']
    no_input = True

    selected_option = prompt_choice_for_config(cookiecutter_dict, env, key, options, no_input)
    assert selected_option == "Chocolate_Chip_Cookie_template"

