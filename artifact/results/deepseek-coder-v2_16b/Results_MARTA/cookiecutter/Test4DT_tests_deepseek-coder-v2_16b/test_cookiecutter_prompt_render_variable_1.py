
import pytest
from jinja2 import Environment
from cookiecutter.prompt import render_variable

@pytest.mark.parametrize("env, raw, cookiecutter_dict, expected_output", [
    (Environment(), "{{ cookiecutter.project_name.replace(' ', '_') }}", {'project_name': 'Peanut Butter Cookie'}, 'Peanut_Butter_Cookie'),
    (Environment(), { 'key1': '{{ cookiecutter.var1 }}', 'key2': '{{ cookiecutter.var2 }}' }, {'var1': 'value1', 'var2': 'value2'}, {'key1': 'value1', 'key2': 'value2'}),
    (Environment(), None, {}, None)
])
def test_render_variable(env, raw, cookiecutter_dict, expected_output):
    result = render_variable(env, raw, cookiecutter_dict)
    assert result == expected_output
