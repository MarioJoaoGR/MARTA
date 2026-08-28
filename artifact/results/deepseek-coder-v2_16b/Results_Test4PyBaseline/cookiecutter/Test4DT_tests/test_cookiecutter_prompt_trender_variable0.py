
import pytest
from jinja2 import Environment
from cookiecutter.prompt import render_variable

# Create a Jinja2 environment for testing
env = Environment()

def test_render_simple_variable():
    cookiecutter_dict = {'project_name': 'Peanut Butter Cookie'}
    raw = "{{ cookiecutter.project_name.replace(' ', '_') }}"
    result = render_variable(env, raw, cookiecutter_dict)
    assert result == "Peanut_Butter_Cookie"

def test_render_nested_structure():
    cookiecutter_dict = {'var2': 'Peanut Butter', 'nested_val': 'Sandwich'}
    raw = {
        'var1': '{{ cookiecutter.var2 }}',
        'var3': {'nested_var': '{{ cookiecutter.nested_val }}'}
    }
    expected_output = {
        'var1': 'Peanut Butter',
        'var3': {'nested_var': 'Sandwich'}
    }
    result = render_variable(env, raw, cookiecutter_dict)
    assert result == expected_output

def test_render_list():
    cookiecutter_dict = {'item1': 'Peanut', 'item2': 'Butter'}
    raw = ['{{ cookiecutter.item1 }}', '{{ cookiecutter.item2 }}']
    expected_output = ['Peanut', 'Butter']
    result = render_variable(env, raw, cookiecutter_dict)
    assert result == expected_output

def test_render_none():
    cookiecutter_dict = {}
    raw = None
    result = render_variable(env, raw, cookiecutter_dict)
    assert result is None

def test_render_complex_structure():
    cookiecutter_dict = {'var2': 'Peanut Butter', 'nested_val': 'Sandwich'}
    raw = {
        'var1': '{{ cookiecutter.var2 }}',
        'var3': {'nested_var': '{{ cookiecutter.nested_val }}'},
        'list_var': ['item1', 'item2']
    }
    expected_output = {
        'var1': 'Peanut Butter',
        'var3': {'nested_var': 'Sandwich'},
        'list_var': ['{{ cookiecutter.item1 }}', '{{ cookiecutter.item2 }}']
    }
    result = render_variable(env, raw, cookiecutter_dict)