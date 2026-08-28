
from unittest.mock import patch
from collections import OrderedDict

# Assuming prompt_for_config is in a module named cookiecutter.prompt, adjust the import if necessary
from cookiecutter.prompt import prompt_for_config


@patch('cookiecutter.prompt.render_variable')
@patch('cookiecutter.prompt.read_user_variable')
@patch('cookiecutter.prompt.read_user_dict')
def test_prompt_for_config_no_input(mock_read_user_dict, mock_read_user_variable, mock_render_variable):
    context = {
        'cookiecutter': {
            'project_name': 'My Project',
            'repo_name': ['my_project', '{{ cookiecutter.project_name.replace(" ", "_") }}'],
            '_private_var': 'hidden_value',
            '__special_var': 'special_{{ cookiecutter.project_name }}'
        }
    }

    mock_render_variable.side_effect = lambda env, raw, context: raw if not isinstance(raw, list) else raw[0]

    result = prompt_for_config(context, no_input=True)

    assert isinstance(result, OrderedDict)