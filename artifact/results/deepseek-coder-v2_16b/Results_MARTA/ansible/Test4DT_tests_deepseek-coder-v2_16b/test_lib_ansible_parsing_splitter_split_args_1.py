
import pytest
from ansible.parsing.splitter import split_args
from ansible.errors import AnsibleParserError


def test_normal_arguments():
    args = 'a=b c="foo bar"'
    expected_output = ['a=b', 'c="foo bar"']
    assert split_args(args) == expected_output

def test_escaped_arguments():
    args = 'arg1=value1 arg2="another value" \\'
    expected_output = ['arg1=value1', 'arg2="another value"']
    assert split_args(args) == expected_output

def test_jinja2_template_context():
    args = '{{ var }} = {{ other_var }}'
    expected_output = ['{{ var }}', '=', '{{ other_var }}']
    assert split_args(args) == expected_output