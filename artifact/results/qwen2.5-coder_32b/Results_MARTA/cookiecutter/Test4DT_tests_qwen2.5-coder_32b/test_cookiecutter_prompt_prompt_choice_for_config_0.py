
import pytest
from jinja2 import Environment
from cookiecutter.prompt import prompt_choice_for_config

def render_variable(env, raw, cookiecutter_dict):
    template = env.from_string(raw)
    return template.render(cookiecutter=cookiecutter_dict)

def read_user_choice(key, rendered_options):
    # Simulate user choice by returning the first option
    return rendered_options[0]




def test_valid_inputs_no_input_true():
    # Case 4: Valid inputs and no_input is True
    cookiecutter_dict = {'project_name': 'Chocolate Chip Cookie'}
    env = Environment()
    key = 'base_template'
    options = ["{{ cookiecutter.project_name.replace(' ', '_') }}_template", 'default_template']
    no_input = True

    selected_option = prompt_choice_for_config(cookiecutter_dict, env, key, options, no_input)
    assert selected_option == "Chocolate_Chip_Cookie_template"
