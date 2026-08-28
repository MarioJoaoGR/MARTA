
# Module: ansible.parsing.splitter
from ansible.parsing.splitter import split_args
import pytest
from ansible.errors import AnsibleParserError

# Test cases for split_args function
def test_split_args_empty():
    args = ''
    expected_output = []
    assert split_args(args) == expected_output

def test_split_args_no_spaces():
    args = 'a=b'
    expected_output = ['a=b']
    assert split_args(args) == expected_output

def test_split_args_with_quotes():
    args = 'c="foo bar"'
    expected_output = ['c="foo bar"']
    assert split_args(args) == expected_output

def test_split_args_nested_jinja2():
    args = 'a=b c={{ var }} d="foo {{ bar }}" e={% set x = 1 %}{{ x }} baz'
    expected_output = ['a=b', 'c={{ var }}', 'd="foo {{ bar }}"', 'e={% set x = 1 %}{{ x }} baz']