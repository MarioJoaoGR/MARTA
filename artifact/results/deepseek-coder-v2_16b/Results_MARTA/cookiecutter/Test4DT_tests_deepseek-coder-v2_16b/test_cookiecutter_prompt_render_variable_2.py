
import pytest
from jinja2 import Environment
from cookiecutter.prompt import render_variable

def test_render_variable_with_template():
    env = Environment()
    raw = "{{ cookiecutter.project_name.replace(' ', '_') }}"
    cookiecutter_dict = {'project_name': 'Peanut Butter Cookie'}
    expected = 'Peanut_Butter_Cookie'
    
    result = render_variable(env, raw, cookiecutter_dict)
    assert result == expected

def test_render_variable_with_dictionary():
    env = Environment()
    raw_dict = {'key1': '{{ cookiecutter.var1 }}', 'key2': '{{ cookiecutter.var2 }}'}
    cookiecutter_dict = {'var1': 'value1', 'var2': 'value2'}
    expected = {'key1': 'value1', 'key2': 'value2'}
    
    result = render_variable(env, raw_dict, cookiecutter_dict)
    assert result == expected

def test_render_variable_with_list():
    env = Environment()
    raw_list = ['{{ cookiecutter.var3 }}', '{{ cookiecutter.var4 }}']
    cookiecutter_dict = {'var3': 'Value3', 'var4': 'Value4'}
    expected = ['Value3', 'Value4']
    
    result = render_variable(env, raw_list, cookiecutter_dict)
    assert result == expected

def test_render_none():
    env = Environment()
    raw = None
    cookiecutter_dict = {}
    expected = None
    
    result = render_variable(env, raw, cookiecutter_dict)
    assert result == expected

def test_render_non_string():
    env = Environment()
    raw = 12345
    cookiecutter_dict = {}
    expected = '12345'
    
    result = render_variable(env, raw, cookiecutter_dict)
    assert result == expected
