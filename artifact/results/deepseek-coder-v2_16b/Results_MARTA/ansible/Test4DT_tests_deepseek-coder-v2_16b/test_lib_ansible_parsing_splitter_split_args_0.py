
import pytest
from ansible.parsing.splitter import split_args
from ansible.errors import AnsibleParserError


def test_simple_string():
    args = 'a=b c="foo bar"'
    expected = ['a=b', 'c="foo bar"']
    result = split_args(args)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_escaped_string():
    args = 'arg1=value1 arg2="another value" \\'
    expected = ['arg1=value1', 'arg2="another value"']
    result = split_args(args)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_jinja2_template():
    args = '{{ var }} = {{ other_var }}'
    expected = ['{{ var }}', '=', '{{ other_var }}']
    result = split_args(args)
    assert result == expected, f"Expected {expected}, but got {result}"